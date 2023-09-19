import os

from autoconf.dictable import to_dict

import autofit as af

from autogalaxy.analysis.analysis import Analysis
from autogalaxy.cosmology.lensing import LensingCosmology
from autogalaxy.cosmology.wrap import Planck15
from autogalaxy.quantity.model.visualizer import VisualizerQuantity
from autogalaxy.quantity.dataset_quantity import DatasetQuantity
from autogalaxy.quantity.model.result import ResultQuantity
from autogalaxy.quantity.fit_quantity import FitQuantity

from autogalaxy import exc


class AnalysisQuantity(Analysis):
    def __init__(
        self,
        dataset: DatasetQuantity,
        func_str: str,
        cosmology: LensingCosmology = Planck15(),
    ):
        """
        Fits a galaxy model to a quantity dataset via a non-linear search.

        The `Analysis` class defines the `log_likelihood_function` which fits the model to the dataset and returns the
        log likelihood value defining how well the model fitted the data.

        It handles many other tasks, such as visualization, outputting results to hard-disk and storing results in
        a format that can be loaded after the model-fit is complete.

        This class is used for model-fits which fit derived quantity of galaxies, for example their
        convergence, potential or deflection angles, to another model for that quantity. For example, one could find
        the `PowerLaw` mass profile model that best fits the deflection angles of an `NFW` mass profile.

        The `func_str` input defines what quantity is fitted, it corresponds to the function of the model `Plane`
        objects that is called to create the model quantity. For example, if `func_str="convergence_2d_from"`, the
        convergence is computed from each model `Plane`.

        This class stores the settings used to perform the model-fit for certain components of the model (e.g. the
        Cosmology used for the analysis).

        Parameters
        ----------
        dataset
            The `DatasetQuantity` dataset that the model is fitted too.
        func_str
            A string giving the name of the method of the input `Plane` used to compute the quantity that fits
            the dataset.
        cosmology
            The Cosmology assumed for this analysis.
        """
        super().__init__(cosmology=cosmology)

        self.dataset = dataset
        self.func_str = func_str

    def log_likelihood_function(self, instance: af.ModelInstance) -> float:
        """
        Given an instance of the model, where the model parameters are set via a non-linear search, fit the model
        instance to the quantity's dataset.

        This function returns a log likelihood which is used by the non-linear search to guide the model-fit.

        For this analysis class, this function performs the following steps:

        1) Use the input quantity of the analysis to determine the function that is passed to `FitQuantity`, which
           generates the quantity from the model which is compared to data.

        2) Use this function to create a `FitQuantity` object, which performs steps such as creating the `model_data`
           of the quantity and computing residuals, a chi-squared statistic and the log likelihood.

        Certain models will fail to fit the dataset and raise an exception. For example if extreme values of the model
        create numerical infinities. In such circumstances the model is discarded and its likelihood value is passed to
        the non-linear search in a way that it ignores it (for example, using a value of -1.0e99).

        Parameters
        ----------
        instance
            An instance of the model that is being fitted to the data by this analysis (whose parameters have been set
            via a non-linear search).

        Returns
        -------
        float
            The log likelihood indicating how well this model instance fitted the imaging data.
        """

        try:
            fit = self.fit_quantity_for_instance(instance=instance)

            return fit.figure_of_merit
        except (exc.GridException, ValueError) as e:
            raise exc.FitException from e

    def fit_quantity_for_instance(self, instance: af.ModelInstance) -> FitQuantity:
        """
        Given a model instance create a `FitImaging` object.

        This function is used in the `log_likelihood_function` to fit the model to the imaging data and compute the
        log likelihood.

        Parameters
        ----------
        instance
            An instance of the model that is being fitted to the data by this analysis (whose parameters have been set
            via a non-linear search).

        Returns
        -------
        FitQuantity
            The fit of the plane to the imaging dataset, which includes the log likelihood.
        """

        plane = self.plane_via_instance_from(instance=instance)

        return FitQuantity(
            dataset=self.dataset, light_mass_obj=plane, func_str=self.func_str
        )

    def visualize(
        self,
        paths: af.DirectoryPaths,
        instance: af.ModelInstance,
        during_analysis: bool,
    ):
        """
        Output images of the maximum log likelihood model inferred by the model-fit. This function is called throughout
        the non-linear search at regular intervals, and therefore provides on-the-fly visualization of how well the
        model-fit is going.

        The visualization performed by this function includes:

        - Images of the best-fit `Plane`, including the images of each of its galaxies.

        - Images of the best-fit `FitQuantity`, including the model-image, residuals and chi-squared of its fit to
        the imaging data.

        The images output by this function are customized using the file `config/visualize/plots.ini`.

        Parameters
        ----------
        paths
            The PyAutoFit paths object which manages all paths, e.g. where the non-linear search outputs are stored,
            visualization, and the pickled objects used by the aggregator output by this function.
        instance
            An instance of the model that is being fitted to the data by this analysis (whose parameters have been set
            via a non-linear search).
        during_analysis
            If True the visualization is being performed midway through the non-linear search before it is finished,
            which may change which images are output.
        """

        if os.environ.get("PYAUTOFIT_TEST_MODE") == "1":
            return

        fit = self.fit_quantity_for_instance(instance=instance)

        visualizer = VisualizerQuantity(visualize_path=paths.image_path)
        visualizer.visualize_fit_quantity(fit=fit)

    def make_result(
        self,
        samples: af.SamplesPDF,
    ) -> ResultQuantity:
        """
        After the non-linear search is complete create its `ResultQuantity`, which includes:

        - The samples of the non-linear search (E.g. MCMC chains, nested sampling samples) which are used to compute
        the maximum likelihood model, posteriors and other properties.

        - The model used to fit the data, which uses the samples to create specific instances of the model (e.g.
        an instance of the maximum log likelihood model).

        - The non-linear search used to perform the model fit.

        The `ResultQuantity` object contains a number of methods which use the above objects to create the max
        log likelihood `Plane`, `FitQuantity`,etc.

        Parameters
        ----------
        samples
            A PyAutoFit object which contains the samples of the non-linear search, for example the chains of an MCMC
            run of samples of the nested sampler.
        search
            The non-linear search used to perform this model-fit.

        Returns
        -------
        ResultQuantity
            The result of fitting the model to the imaging dataset, via a non-linear search.
        """
        return ResultQuantity(samples=samples, analysis=self)

    def save_attributes(self, paths: af.DirectoryPaths):
        """
        Before the non-linear search begins, this routine saves attributes of the `Analysis` object to the `pickles`
        folder such that they can be loaded after the analysis using PyAutoFit's database and aggregator tools.

        For this analysis, it uses the `AnalysisDataset` object's method to output the following:

        - The dataset's data.
        - The dataset's noise-map.
        - The settings associated with the dataset.
        - The Cosmology.
        - Its mask.

        It is common for these attributes to be loaded by many of the template aggregator functions given in the
        `aggregator` modules. For example, when using the database tools to perform a fit, the default behaviour is for
        the dataset, settings and other attributes necessary to perform the fit to be loaded via the pickle files
        output by this function.

        Parameters
        ----------
        paths
            The PyAutoFit paths object which manages all paths, e.g. where the non-linear search outputs are stored,
            visualization, and the pickled objects used by the aggregator output by this function.
        """
        paths.save_fits(
            name="data",
            hdu=self.dataset.data.hdu_for_output,
            prefix="dataset",
        )
        paths.save_fits(
            name="noise_map",
            hdu=self.dataset.noise_map.hdu_for_output,
            prefix="dataset",
        )
        paths.save_fits(
            name="mask",
            hdu=self.dataset.mask.hdu_for_output,
            prefix="dataset",
        )
        paths.save_json(
            name="cosmology",
            object_dict=to_dict(self.cosmology),
        )
