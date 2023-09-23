import jax
import jax.numpy as jnp

import optax

def params_to_model(params):
    """ convert the parameters into model y and model x

    Parameters:
    -----------
    params: pytreee
        a jax pytree providing 
        - coefs (N,)
        - variables (M, N) 
        - offset ()
    
    Returns
    -------
    list
        - model_y (N,) 
        - model_x (M, N)
    """
    model_y = jnp.dot(params['coefs'], params["variables"]) + params['offset']
    model_x = params["variables"]
    return model_y, model_x

@jax.jit
def loglikelihood(params, observations, errors):
    """ Full likelihood for the "y_j = a^i x_ij + offset" model
    
    There are N values (len(y)) for M variables
    
    Parameters
    ----------
    params: pytree
        a jax pytree providing:
        - coefs  (M,)
        - offset ()
        - sigma ()
        - variables (M, N)
        
    observed: list
        observed data with the format (y, x):
        - y (N,)
        - x (M, N)
        
    errors: pytree
        pytree containing the observation errors
        - y_err (N,)
        - x_err (M, N)
        
    Returns
    -------
    float
    """
    # comment information: N=number of targets, M=number variables

    # Observations
    observed_y, observed_x = observations      # (N,), (M, N)
    model_y, model_x = params_to_model(params) # (N,), (M, N)
    ntargets_ = len(model_y) # this is N
    
    y_err, x_err = errors
    
    # Covariance should be here.
    sigma2 = params['sigma']**2 + y_err**2 # (N,)
    chi2_y = (observed_y - model_y)**2/ sigma2  # (N,)
    chi2_x = (observed_x - model_x) ** 2 / x_err**2 # (M, N)
    
    # log likelihood | the last term should be ntargets_*jnp.log(sigma2) if sigma2 is a float
    loglikelihood = jnp.sum(chi2_y) + jnp.sum(chi2_x) + jnp.sum(jnp.log(sigma2)) # float
    return loglikelihood
