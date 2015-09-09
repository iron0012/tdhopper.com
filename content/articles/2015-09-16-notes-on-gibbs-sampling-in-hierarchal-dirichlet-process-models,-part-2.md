Title: Notes on Gibbs Sampling in Hierarchal Dirichlet Process Models, Part 2
Date: 2015-09-16 15:34
Slug: notes-on-gibbs-sampling-in-hierarchal-dirichlet-process-models-part-2
Category: Nonparametric Bayes
Tags: IPython, math, statistics, npbayes

[In an earlier post](http://stiglerdiet.com/blog/2015/Sep/11/notes-on-gibbs-sampling-in-hierarchal-dirichlet-process-models/), I derived the necessary equations to sample table assignments when applying the "Posterior sampling in the Chinese restaurant franchise" algorithm to the case of latent Dirichlet allocation. I complete the derivation of necessary equations here.

We need to sample $k_{jt}$ (the dish/topic for table $t$ in restaurant $j$):

\\[\displaystyle
    p(k_{jt}=k \,|\, {\bf t}, {\bf k}^{-jt}) \propto
    \begin{cases}
        m_{\cdot k}^{-jt}\cdot f_k^{-{\bf x}_{jt}}({\bf x}_{jt})
            & {\tiny \text{if } k \text{ previously used,}}\\\\
        \gamma\cdot f_{k^\text{new}}^{-{\bf x}_{jt}}({\bf x}_{jt})
            & {\tiny \text{if } t=k^{\text{new}}}.
    \end{cases}
\\]

where $f_k^{-{\bf x}\_{jt}}({\bf x}\_{jt})$ is the "conditional density of ${\bf x}\_{jt}$ given all data items associated with mixture component $k$ leaving out ${\bf x}\_{jt}$" (Teh, et al). (${\bf x}\_{jt}$ is every customer in restaurant $j$ seated at table $t$). $m_{\cdot k}^{-jt}$ is the number of tables (in all franchises) serving dish $k$ when we remove table $jt$.

This requires $f_k^{-{\bf x}\_{jt}}({\bf x}\_{jt})$; this is different from Equation (30), though they look quite similar.

\\[
\begin{array}{rl}
    f_k^{-{\bf x}_{jt}}({\bf x}_{jt})
    &=\frac{\displaystyle
            \int
                {\prod_{x_{ji}\in {\bf x}_{jt}}}
                f(x_{ji} \,|\, \phi_k)
                   \left[
                   \prod_{x_{i'j'}\not\in {\bf x}_{jt}, z_{i'j'}=k}
                        f(x_{j'i'} \,|\, \phi_k)
                   \right]
                        h(\phi_k)
                        d\phi_k
        }
        {\displaystyle
            \int
                \left[
                    \displaystyle\prod_{x_{i'j'}\not\in {\bf x}_{jt}, z_{i'j'}=k}
                    f(x_{i'j'}|\phi_k)
                \right]
                h(\phi_k)d\phi_k
        } \\\\
    &=\frac{\displaystyle
            \int
                {\prod_{x_{ji}\in {\bf x}_{jt}}}
                \phi_{k x_{ji}}
                   \left[
                   \prod_{x_{i'j'}\not\in {\bf x}_{jt}, z_{i'j'}=k}
                        \phi_{k x_{i'j'}}
                   \right]
                        \prod_{w}
                    \phi_{kw}^{\beta-1}
                        d\phi_k
        }
        {\displaystyle
            \int
                \left[
                    \displaystyle\prod_{x_{i'j'}\not\in {\bf x}_{jt}, z_{i'j'}=k}
                    f(x_{i'j'}|\phi_k)
                \right]
                \prod_{w}
                    \phi_{kw}^{\beta-1}
                    d\phi_k
        } \\\\
    &=\frac{\displaystyle
            \int
                {\prod_{x_{ji}\in {\bf x}_{jt}}}
                \phi_{k x_{ji}}
                   \left[
                   \prod_{x_{i'j'}\not\in {\bf x}_{jt}, z_{i'j'}=k}
                        \phi_{k x_{i'j'}}
                   \right]
                        \prod_{w}
                    \phi_{kw}^{\beta-1}
                        d\phi_k
        }
        {\displaystyle
            \int
                \left[
                    \displaystyle\prod_{x_{i'j'}\not\in {\bf x_{jt}}, z_{i'j'}=k}
                    \phi_{k x_{i'j'}}
                \right]
                \prod_{w}
                    \phi_{kw}^{\beta-1}
                    d\phi_k
        }
\end{array}
\\]

The denominator is

\\[
\begin{align}
    \text{denominator}&=
    \int\left[
        \prod_{x_{i'j'}\not\in {\bf x_{jt}}, z_{i'j'}=k}
        \phi_{k x_{i'j'}}
    \right]
    \prod_{w}
        \phi_{kw}^{\beta-1}
        d\phi_k \\\\
    &=\int\left[
        \prod_w \phi_{kw}^{n_{kw}^{-jt}} \prod_w \phi_{kw}^{\beta-1}
    \right]
        d\phi_k \\\\
    &=\int\left[
        \prod_w \phi_{kw}^{n_{kw}^{-jt}+\beta-1}
    \right]
        d\phi_k \\\\
    &=\frac{
        \prod_w \Gamma\left(
            n_{kw}^{-jt} + \beta
        \right)
    }{
        \Gamma\left( \sum_w
            n_{kw}^{-jt}+\beta
        \right)
    } \\\\
    &=\frac{
        \prod_w \Gamma\left(
            n_{kw}^{-jt} + \beta
        \right)
    }{
        \Gamma\left(
            n_{k\cdot}^{-jt}+V\beta
        \right)
    }
\end{align}
\\]

The numerator is

\\[
\begin{align}
    \text{numerator}
    &=\int
    {\prod_{x_{ji}\in {\bf x}_{jt}}}
    \phi_{k x_{ji}}
       \left[
       \prod_{x_{i'j'}\not\in {\bf x}_{jt}, z_{i'j'}=k}
            \phi_{k x_{i'j'}}
       \right]
            \prod_{w}
        \phi_{kw}^{\beta-1}
            d\phi_k \\\\
    &=\int
    \prod_{w}
        \phi_{kw}^{
            n_{kw}^{-jt} +
            n_{\cdot w}^{jt} +
            \beta + 1
            }
        d\phi_k \\\\
    &=\frac{
       \prod_w \Gamma\left(
           n_{kw}^{-jt} + n_{\cdot w}^{jt} + \beta
       \right)
    }{
      \Gamma \left(
        \sum_w
        n_{kw}^{-jt} + n_{\cdot w}^{jt} + \beta
      \right)
    }\\\\
    &=\frac{
       \prod_w \Gamma\left(
           n_{kw}^{-jt} + n_{\cdot w}^{jt} + \beta
       \right)
    }{
      \Gamma \left(
        n_{k\cdot}^{-jt} + n_{\cdot \cdot}^{jt} + \beta
      \right)
    }
\end{align}
\\]

This gives us a closed form version of this conditional distribution:

\\[
\begin{array}{rl}
    f_k^{-{\bf x}_{jt}}({\bf x}_{jt})
    &= \displaystyle\frac{
       \prod_w \Gamma\left(
           n_{kw}^{-jt} + n_{\cdot w}^{jt} + \beta
       \right)
    }{
            \prod_w \Gamma\left(
                n_{kw}^{-jt} + \beta
            \right)
        }
    \frac{
            \Gamma\left(
                n_{k\cdot}^{-jt}+V\beta
            \right)
        }{
      \Gamma \left(
        n_{k\cdot}^{-jt} + n_{\cdot \cdot}^{jt} + \beta
      \right)
    }
\end{array}
\\]

We also need the conditional distribution of $k$ is a new dish: $f_{k^\text{new}}^{-{\bf x}\_{jt}}({\bf x}\_{jt})$. Shuyo provides without derivation:

\\[
\begin{align}
f_{k^\text{new}}^{-{\bf x}_{jt}}({\bf x}_{jt})
    &=\int
        \left[
        \prod_{x_{ji}\in \mathbf{x_{jt}}}
            f(x_{ji} \,|\, \phi)
        \right]
        h(\phi)d\phi_k
        \\\\
    &=\int
        \prod_{x_{ji}\in \mathbf{x_{jt}}}
            \phi_{x_{ji}}
        \cdot
        \frac{
                \Gamma(V\beta)
            }{
                \prod_w \Gamma(\beta)
        }
        \prod_w \phi_w^{\beta-1}
        d\phi \\\\
    &=\frac{
                \Gamma(V\beta)
            }{
                \prod_w \Gamma(\beta)
        }
        \int
            \prod_{x_{ji}\in \mathbf{x_{jt}}}
            \phi_{x_{ji}}
            \cdot
            \prod_w \phi_w^{\beta-1}
        d\phi\\\\
    &=\frac{
                \Gamma(V\beta)
            }{
                \prod_w \Gamma(\beta)
        }
        \int
            \prod_{x_{ji}\in \mathbf{x_{jt}}}
                \phi_{x_{ji}}^{\left(\beta+1\right)-1}
            \cdot
            \prod_{x_{jt}\not\in \mathbf{x_{jt}}} \phi_{x_{jt}}^{\beta-1}
        d\phi\\\\
    &=\frac{
                \Gamma(V\beta)
            }{
                \prod_w \Gamma(\beta)
        }\cdot
        \frac{
            \prod_{x_{ji}\in \mathbf{x_{jt}}}
                \Gamma(\beta+1)
            \prod_{x_{ji}\not\in \mathbf{x_{jt}}}\Gamma(\beta)
            }{
            \Gamma(V\beta+\sum_{x_{ji}\in \mathbf{x_{jt}}} 1)
        }\\\\
    &=\frac{
        \Gamma(V\beta)
        \prod_v \Gamma(\beta+n_{\cdot v}^{jt})
    }{
        \Gamma(V\beta+n_{\cdot\cdot}^{jt})
        \prod_v \Gamma(\beta)
    }
\end{align}
\\]

Given these equations for $f_{k}^{-{\bf x}\_{jt}}({\bf x}\_{jt})$ and $f_{k^\text{new}}^{-{\bf x}\_{jt}}({\bf x}\_{jt})$, we can draw samples from $p(k_{jt}=k \,|\, {\bf t}, {\bf k}^{-jt})$ by enumeration over topics. Combined with sampling from table assignment [described here](http://stiglerdiet.com/blog/2015/Sep/11/notes-on-gibbs-sampling-in-hierarchal-dirichlet-process-models/), we now have a complete Gibbs sampler for the [Posterior sampling in the Chinese restaurant franchise in Teh, et al.](http://www.cs.berkeley.edu/~jordan/papers/hdp.pdf)