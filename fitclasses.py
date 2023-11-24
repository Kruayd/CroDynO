"""Module containing the base class for cross section fits and all its derived
subclasses.

References
----------
- [1] ATOMIC DATA FOR FUSION VOLUME 1 COLLISIONS OF H, H2, He and Li ATOMS and
IONS with ATOMS and MOLECULES. C. F. Barnett

Notes
-----
Each class inheriting from `CrossSectionFit` must be added to this module and
must redefine the `_fit_function` property.
This module uses cross sections expressed in square meters and energies
expressed in eV.

"""
from abc import ABCMeta, abstractmethod
from typing import Iterable
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.axes import Axes


class CrossSectionFit(metaclass=ABCMeta):
    """Base class for cross section fits.

    Notes
    -----
    All CroDynO fits are subclasses of `CrossSectionFit` and must be added to
    the `fitclasses.py` module

    Parameters
    ----------
    domain : (2,) array_like (eV)
        Boundaries of the domain in which the fit is valid.

    description : string
        Description of the process and additional notes.

    energy_space : int_like, float_like or (n,) array_like, optional (eV)
        Value or array used to initialize the `energy_space` property. Default
        is 5000. See the `energy_space` property and setter method.

    Attributes & Properties
    -----------------------
    domain : tuple (eV)
        Boundaries of the domain in which the fit function is valid.

    description : string
        Description of the process and additional notes.

    energy_space : ndarray (eV)
        Array of energy values used to calculate cross section.

    Methods
    -------
    __call__(energies=None)
        Call self as a function and evaluate cross section.

    energy_space.setter(value)
        Setter method for the `energy_space` attribute.

    plot(ax=None, *args, **kwargs)
        Plot the evaluated cross section.

    """

    def __init__(self, domain, description, energy_space=5000):

        # Ensure domain is a valid iterable of length 2
        if not isinstance(domain, Iterable) or len(domain) != 2 or domain[0] >\
           domain[1]:
            raise TypeError('Domain must be an ordered Iterable of length 2')
        # Ensure description is a string
        if not isinstance(description, str):
            raise TypeError('Description must be a string')

        # Assign _domain and energy_space attributes
        # _sigma is assigned by the energy_space setter method
        self._domain = tuple(domain)
        self._description = description
        self.energy_space = energy_space

    def __call__(self, energies=None):
        """Call self as a function and evaluate cross section.

        Parameters
        ----------
        energies : int_like, float_like or (n,) array_like, optional (eV)
            Energies against which to evaluate cross section.

        Returns
        -------
        ndarray or float (m^2)
            Evaluated cross section.

        Notes
        -----
        This method calls the property `_fit_function` as a function, which is
        implemented as an abstract method and therefore it is mandatory to
        redifine in each sublcass that inherits from `CrossSectionFit`.

        """
        # If energies are provided, update energy_space
        # The energy_space setter also sets _sigma to None
        if energies is not None:
            self.energy_space = energies
        # If cross section has not been evaluated, evaluate it
        if self._sigma is None:
            self._sigma = self._fit_function(self._energy_space)
        # If both conditions are not met, there's no need to evaluate _sigma
        # again
        return self._sigma

    @property
    @abstractmethod
    def _fit_function(self):
        pass

    @property
    def domain(self):
        return self._domain

    @property
    def description(self):
        return self._description

    @property
    def energy_space(self):
        return self._energy_space

    @energy_space.setter
    def energy_space(self, value):
        """Setter method for the `energy_space` attribute.

        Parameters
        ----------
        value : int_like, float_like or (n,) array_like
            If value is an integer, `energy_space` is set to a log-spaced array
            between the boundaries of the domain. If value is a float or an
            array-like, energy_space is set equal to it.

        """
        # Reset sigma to None since energy_space has changed
        self._sigma = None
        # Check if value is an integer
        if isinstance(value, (int, np.integer)):
            # Generate a log-spaced array between the domain boundaries
            self._energy_space = np.logspace(*np.log10(self._domain), value,
                                             dtype=np.float64)
        else:
            try:
                # Convert to array and filter forbidden values
                value = np.asarray(value, dtype=np.float64)
                if value.ndim > 1:
                    raise TypeError('Array must be a one-dimensional array or '
                                    'a float')
                self._energy_space = self._allowed_energies(value)
            except Exception as e:
                raise TypeError('Invalid type provided for '
                                f'{type(self).__name__}.energy_space') from e
        # Save value for __repr__ method
        self._energy_repr = value

    def _allowed_energies(self, energy_space):
        """Filters out forbidden energy values.

        Parameters
        ----------
        energy_space : ndarray
            If `energy_space` is an array, removes forbidden energy values. If
            it is a scalar, checks if it is within the domain.

        Returns
        -------
        ndarray or None
            Original `energy_space` parameter stripped of forbidden values.

        """
        # If energy_space is a scalar, check if it is within the domain
        # boundaries
        if energy_space.ndim == 0:
            return energy_space.copy() if self.domain[0] <= energy_space <=\
                   self.domain[1] else None
        else:
            # If energy_space is an array, filter out values outside the domain
            # boundaries
            valid_energies = energy_space[(energy_space >= self.domain[0]) &
                                          (energy_space <= self.domain[1])]
            return valid_energies.copy() if valid_energies.size > 0 else None

    def plot(self, ax=None, *args, **kwargs):
        """Plot cross section against energy values.

        Parameters
        ----------
        ax : Axes, optional
            The matplotlib.axes.Axes object that must plot the data. If none is
            given, matplotlib.pyplot.loglog is used instead.

        Returns
        -------
        list of Line2D
            A list of lines representing the plotted data.

        """
        if ax is None:
            # If no axes provided, use pyplot's loglog
            return plt.loglog(self.energy_space, self(),
                              *args, **kwargs)
        elif isinstance(ax, Axes):
            # If Axes instance provided, use its loglog method
            return ax.loglog(self.energy_space, self(), *args,
                             **kwargs)
        else:
            raise TypeError('ax must be a valid matplotlib.axes.Axes')

    def __repr__(self):
        return f"CrossSectionFit({self._domain}, '{self._description}', "\
               f"energy_space={repr(self._energy_repr)})"

    def __str__(self):
        return self._description


class BarnettChebFit(CrossSectionFit):
    """Subclass for Chebyshev polynomial fit as it is described in Appendix 1
    of ATOMIC DATA FOR FUSION VOLUME 1 COLLISIONS OF H, H2, He and Li ATOMS and
    IONS with ATOMS and MOLECULES by C. F. Barnett

    Notes
    -----
    Barnett fits cross sections data with a function of the type
    f(e) = exp(T(ln(e))), where T is a Chebyshev polynomial of the first kind
    and e is the energy per unit mass of the projectile (in the target
    reference frame) expressed in eV/amu. The T0 coefficient given by Barnett
    doesn't actually correspond to the T0 Chebyshev coefficient, but actually
    to its double. Additionaly, the cross section is expressed in square
    centimeters. This class automatically converts to square meters and eV.

    Parameters
    ----------
    domain : (2,) array_like (eV/amu)
        Boundaries of the domain in which the fit is valid.

    description : string
        Description of the process and additional notes.

    projectile_mass : scalar (amu)
        Scalar used to convert from eV/amu to just eV.

    energy_space : int_like, float_like or (n,) array_like, optional (eV)
        Value or array used to initialize the `energy_space` property. Default
        is 5000. See the `energy_space` property and setter method.

    Attributes & Properties
    -----------------------
    domain : tuple (eV)
        Boundaries of the domain in which the fit function is valid.

    description : string
        Description of the process and additional notes.

    energy_space : ndarray (eV)
        Array of energy values used to calculate cross section.

    barnett_coefficients : tuple
        Fit coefficients reported by Barnett.

    chebyshev_coefficients : tuple
        Actual coefficients for the Chebyshev polynomial.

    chebyshev_domain (ln(eV))
        Domain of the Chebyshev polynomial.

    """

    def __init__(self, domain, description, projectile_mass,
                 barnett_coefficients, energy_space=5000):

        # Ensure projectile_mass is a scalar
        if not np.isscalar(projectile_mass):
            raise TypeError('Projectile mass must be a scalar')

        # Initialize base class instance
        super().__init__(np.array(domain) * projectile_mass, description,
                         energy_space=energy_space)
        # Ensure barnett_coefficients is a valid iterable that can be cast to a
        # numeric ndarray
        if not isinstance(barnett_coefficients, Iterable):
            raise ValueError('Barnett coefficients must be a valid Iterable')
        barnett_coefficients = np.asarray(barnett_coefficients,
                                          dtype=np.float64)
        # Assign _barnett_coefficients
        self._barnett_coefficients = tuple(barnett_coefficients)
        # First Barnett coefficient is double the corresponding Chebyshev
        # coefficient
        barnett_coefficients[0] /= 2
        # Generate the Chebyshev polynomial
        self._cheb_poly = np.polynomial.Chebyshev(barnett_coefficients,
                                                  domain=np.log(self._domain))
        # Assign _chebyshev_coefficients, _chebyshev_domain and
        # _projectile_mass
        self._chebyshev_coefficients = tuple(self._cheb_poly.coef)
        self._chebyshev_domain = tuple(self._cheb_poly.domain)
        self._projectile_mass = projectile_mass

    @property
    def barnett_coefficients(self):
        return self._barnett_coefficients

    @property
    def chebyshev_coefficients(self):
        return self._chebyshev_coefficients

    @property
    def chebyshev_domain(self):
        return self._chebyshev_domain

    @property
    def _fit_function(self):
        # Barnett cross sections are give in cm^2 but we want m^2
        return lambda x: np.exp(self._cheb_poly(np.log(x)))/1e4

    def __repr__(self):
        domain = (self._domain[0] / self._projectile_mass,
                  self._domain[1] / self._projectile_mass)
        return f"BarnettChebFit({domain}, '{self._description}', "\
               f"{self._projectile_mass}, {self._barnett_coefficients}, "\
               f"energy_space={repr(self._energy_repr)})"
