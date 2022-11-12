# This course is about:

***The science of good measurement***

__Good means low uncertainty__


## Uncertainty

<img src="fig/uncertainty-ahead.jpg" alt="image" />

## Not this kind of “uncertainty”

<img src="fig/uncertainty_arrows.jpg" alt="image" />

## Measurement uncertainty

-   Engineers are interested in the uncertainty of measurement simply
    because we wish to make good quality measurements and to
    **understand** the results.

-   Uncertainty is a **quantification of the doubt about the measurement
    result**.

-   It is important not to confuse the terms "error" and "uncertainty"

**Error $\neq$ uncertainty**

-   Assume a rod of *true value* of 25 mm and a measured value of 24 mm,
    here error is 1 mm.

-   Error is a property of this particular measurement and value.

<img src="fig/rod_length.png" alt="image" height=300px/>



**Uncertainty is a quantification of the doubt about the measurement result**

-   The same rod and the same measured value, but **also** the measured value depends upon environment factor that **makes the doubt** of plus or minus 1 mm.

-   So the true value could be ANYTHING between 23 mm or 25 mm and
    uncertainty is 1 mm.

-   Our goal is to *quantify* and then to *reduce* this uncertainty

<img src="fig/inner_diameter_2.jpg" alt="image" />


## Let’s repeat: error is not uncertainty

<img src="fig/error_vs_uncertainty.png" alt="image" />

Source: https://www.engineering.com/story/an-introduction-to-metrology-and-quality-in-manufacturing

## Definitions

1.  **Measurement is:** estimate of the size, amount or degree of a
    desired quantity/parameter by using a set of instruments or devices.

2.  The result is **the best estimate with uncertainty, expressed in
    standard units**.

<img src="fig/words.png" alt="image" />

based on “Good practice guide no. 131” of **The Institute of Mechanical
Engineers** <https://www.npl.co.uk/resources/gpgs>

## We use only SI

<span style="color:red">International system of units (SI)</span>

-   The International System of Units has the abbreviation SI (French).

-   The SI is at the centre of all modern science and technology and is
    used worldwide to ensure measurements can be standardized
    everywhere.

-   There are tremendous benefits to using SI units and countries
    routinely compare their SI measurement standards.

-   This keeps measurements made in different countries compatible with
    one another.

## Basic units

<img src="fig/units1.png" alt="image" />

## Derived units

<img src="fig/units2.png" alt="image" />

## Measurement science is important 

Aero-engines are built to a very high accuracy and require about
**200,000** separate measurements during production and maintenance

<img src="fig/engine.jpeg" alt="image" />  
<https://www.af.mil/News/Photos/igphoto/2000589434/>

## Categories of experiments

Different categories require different uncertainty approach:

-   basic science - to learn something new about nature

-   applied science - to verify a theoretical model

-   design - to make sure two parts will fit

-   production - to determine the correct price

-   regulation - to check that that an item is within specification:
    pass/fail

In all cases, a measurement is **only** useful if: a) has high quality,
b) if suitable for the **intended purpose**.

Lord Kelvin said once: 

![image](fig/kelvin_quote.jpeg)

## Measurement is as good as its uncertainty

<span style="color:red">measurement = best estimate ± uncertainty</span>

$L = 2.35 \pm 0.03$  mm  (95% confidence)

**We report:** what is measured $L$, its most probable value (2.35), its uncertainty range (0.03) and the best known confidence range (95%)

"If you cannot quantify the measurement uncertainty, **don’t** start make the measurement - it is useless", source: https://blog.beamex.com/calibration-uncertainty-for-dummies-part-1>

## Uncertainty analysis

1.  identify all the possible <span style="color:red">sources</span> of uncertainty,

2.  evaluate the <span style="color:red">standard uncertainty</span> from each source,

3.  <span style="color:red">combine</span> the individual standard uncertainties

## Some known sources of uncertainty

-   Measuring instrument: they suffer from errors.

-   Environmental conditions: some measurements are affected by varying
    in ambient conditions. e.g. calibration of slip gauge depends upon
    the coefficient of thermal expansion.

-   The instrument or gauge’ being measured may change over time.

-   The measurement procedure may be difficult to perform.

-   Operator’s skill: some calibration procedure requires experience
    and/or judgment skill.

You should not make any measurements unless you are aware of the related
uncertainty.

## How to reduce uncertainty?

**It is important to reduce uncertainty for an accurate measurement.**
<span style="color:red">Remember:</span> you cannot eliminate uncertainty

-   Reduce the random effect by repeating the measurement process

-   Use the most suitable measuring instruments

-   Use the calibrated instrument for measurement

-   Apply correction if you know any **systematic effect**

-   Record all the uncertainty components

-   Avoid mistakes by double-checking calculations

-   Check your measurement by different operator or method.

## 8 points plan to quantify uncertainty

<img src="fig/8steps.png" alt="image" />

## 1. Decide what you need to find out from your measurement

Identify the **type of measurement** and how it is to be measured, as
well as any **calculations\*** required in the process such as effects
that require a correction.

For this example, suppose you decide to use a set of electronic calipers
to measure the length of an object.
<img src="fig/caliper.png" alt="image" />

\* **direct** and **indirect** measurements in the Lab

##  2. Carry out and record the measurements needed

Follow a **specified measurement procedure** to ensure that your
measurement is consistent with **standards**. Check: **the zero
reading** on your electronic calipers, you know they are **well
maintained** and **calibrated**, and then you took **repeated
readings**.

<img src="fig/notebook1.png" alt="image" />

## Notebook should be clear

**a date**, **name**, **the instruments**, **a note of the calibration
sticker on the calipers**, and **a record of the temperature**. <span
class="alert">This is good practice and pays off by 5% bonus for lab
notebooks</span>

<img src="fig/notebook1.png" alt="image" />

## Outliers and averaging

-   Because the numbers are laid out neatly, it makes it easy to spot
    that Measurement 3 is out of line with the others. Having confirmed
    with the partners this is **a mistake**, you can cross it out
    without making it illegible.

-   In **statistical terms**, this reading is considered **an outlier**
    and is clearly not part of the natural variability of measurement.
    It is therefore ignored in any further calculations and you simply
    take the average of the other 24.

-   This gives your best estimate of the length as:
    (21.53 + 21.51 + 21.47 + 21.43 + ...)/24 = 21.493 *m**m*

## 3. Evaluate the uncertainty of each input quantity that feeds in to the final result (Type A and Type B evaluations). Express all uncertainties in similar terms (standard uncertainties)

<img src="fig/summaryuncertainty.png" alt="image" />

## Type A uncertainty

-   **Type A** uncertainty evaluations are carried out by **statistical
    methods**, usually from repeated measurement readings. In this case,
    you have 24 readings and have used these to gain an average of
    21.493 mm.

## 3. continued ...

-   **Type B** uncertainty evaluations are carried out using any other
    information such as past experiences, calibration certificates,
    manufacturers specifications, **from calculation**, from published
    information and from common sense. In this example you can consider
    **the calibration of the calipers.**

-   Both of these uncertainties need to be expressed in similar terms so
    that you can **compare and combine** them. So you need to associate
    a number – called a <span style="color:red">“standard
    uncertainty”</span> – with each term.

## Type A uncertainty evaluation

For <span style="color:red">Type A</span>: characterize the variability of
*n* readings by their **standard deviation**, given by the formula below

$$\mathrm{STD} = \sqrt{\frac{\sum\limits_{i=1}^{n} \left( x_i - \bar{x} \right)^2 }{n-1}}$$

$$= \sqrt{\frac{\left( 21.53 - 21.493 \right)^2  + \left( 21.51 - 21.493 \right)^2 + ... }{24 -1 }}  = 0.1044$$

This is <span style="color:red">standard deviation of a single measurement
!</span>

## Write it clear in your notebook 

Of course one could glue (white glue, no marking) a print from a Python
notebook

<img src="fig/notebook2.png" alt="image" />

## Type A standard uncertainty of average

**Average (mean) is the random variable by itself.**

For *n* readings the <span style="color:red">standard uncertainty associated
with the **average**</span>:

<span style="color:red">standard uncertainty</span> = STD / $\sqrt{n}$

The standard uncertainty associated with the average is thus:

$$0.1044\, \mathrm{mm}/\sqrt{24} = 0.021 \mathrm{mm}$$

## Type A standard uncertainty

This uncertainty is based upon the idea that the readings were drawn
from a **normal probability distribution**. Using 24 readings we
estimate **the characteristics of this distribution** – and then worked
out the standard uncertainty – <span style="color:red">how well one can
estimate the position of the centre of the distribution</span>.

<img src="fig/standarduncertainty.png" alt="image" />

## Type B uncertainty evaluation

-   Type B uncertainty evaluation is needed to assess uncertainties
    where statistics are not applicable, **for example** where there are
    <span style="color:red">biases</span> – **errors which always affect the
    reading in the same way**.

-   In order to compare the uncertainty from Type A and Type B
    evaluation you need to convert **the range of the rectangular
    distribution into a standard deviation** to be used as **the
    standard uncertainty**.

Typical sources of Type B

<img src="fig/Vernier-Caliper-6.jpg" alt="image" />

-   Calibration - we do not know what how the calibration was performed

-   Use of different instruments (old/new, different resolutions, etc.)

-   Different operators, human factor

-   Environmental factors, external parameters (electromagnetic noise,
    temperature in the room)

ISO guidelines

ISO guidelines: **assume that any error or bias is a random draw from a
known statistical distribution.**

Then we use the standard deviation from that assumed distribution. Our basic options are:

1.  **Uniform**, all equally probable within the range, zero probability outside

2.  **Triangular**, central more probable within the range

3.  **Student's $t$**, random, all probable, for small $n \lt 20$

4.  **Gaussian or normal**, random, all probable, $n \gt 20$

Probability and distributions
<img src="fig/central-limit-theorem.png" alt="image" />
<https://www.muelaner.com/uncertainty-of-measurement/>

## Uniform distribution

Most conservative estimate of uncertainty, largest standard deviation

We assume that we know the end points

All the effects within the range are equaly likely

$$ f(x)= \frac{1}{B-A} \; \mathrm{for} \; A \leq x \leq B$$

Mean: $\frac{A+B}{2}$ and standard deviation:
$\sqrt{\frac{(B-A)^{2}}{12}}$

When we work with $-a \leq x \leq a$ then we get

$$ s = \frac{1}{\sqrt{3}} a $$

Triangular distribution

-   Less conservative estimate of uncertainty

-   Smaller standard deviation

-   We assume the range and take it symmetric for simplicity:

-   For $-a \leq x \leq a$:

    $$ s=\frac{1}{\sqrt{6}}a $$

### Back to Type B in our example

standard uncertainty = half range/$\sqrt{3}$

-   In this example, the calibration certificate simply states that the
    device will read within  ± 0.02 mm of the correct value, if it is
    used correctly and the temperature is within the range
    0<sup>∘</sup>C to 40<sup>∘</sup>C.

-   The standard uncertainty associated with the calibration of the
    device is thus
    $$0.02 \, \mathrm{mm}/\sqrt{3} = 0.012 \, \mathrm{mm}$$

### Summary of uncertainty types

<img src="fig/summaryuncertainty.png" alt="image" />

### 4. Decide whether the errors of the input quantities are independent of each other 

-   Could a large error in one input cause a large error in another?

-   Could an outside influence such as temperature have a similar effect
    on several aspects of uncertainty at once?

-   If the errors are independent, which is typical and assumed in this
    example, you can use the formula in step 6 to calculate combined
    standard uncertainty. If not, extra calculations are needed, come to
    the next lecture.

<span style="color:red">Assuming that there is no correlation can lead to an
unreliable uncertainty evaluation.</span>

### 5. Calculate the result of your measurement (including any known corrections, such as calibrations)

-   You get your result from the mean reading and by making all
    necessary corrections to it, such as **calibration corrections**
    listed on a calibration certificate or manufacturer’s specifications
    to correct temperature drift, etc.

-   In this example you do not have any certificate corrections to
    include. But if you did, they **would be added to the original mean
    reading** of 21.493 mm.

### 6. Find the combined standard uncertainty from all the individual uncertainty contributions

So in order to evaluate the uncertainty we add the components “in
quadrature” (also known as “the root sum of the squares”). The result of
this is called the “combined standard uncertainty”.

$$u = \sqrt{ \left( p^2 + b^2 \right)}$$

-   Type A -  from the variability of the data, probability *p*

-   Type B -  from the calibration certificate, bias, *b*

### And our combined uncertainty is ... 

$$u = \sqrt{ (0.021)^2 + (0.012)^2} = 0.024 \, \mathrm{mm}$$

The best estimate of the length is the average of the 24 readings. The
associated standard uncertainty is evaluated by combining (in
quadrature) the standard uncertainties relating to the main factors that
could cause the calipers to read incorrectly.

### 7. Calculate expanded uncertainty for a particular level of confidence

-   The combined standard uncertainty is equivalent to <span
    class="alert">one standard deviation</span>, the $\mu \pm 1\sigma$ covers about 68% of the normal distribution.

-   Increase the level of confidence that **the true answer lies within
    a given a range**, by multiplying the standard uncertainty by a
    coverage factor to give an expanded uncertainty:

    $$ U = k \times u $$

-   Expanded uncertainty: increase the confidence level to 95% or even
    99% by combining with the appropriate coverage factor (assuming a
    normal distribution).

<img src="fig/extendeduncertainty.png" alt="image" />

### 8. Write down the measurement result and the uncertainty, and state how you got both of these

<span style="color:red">It is important to express the result in your report
so that a reader/boss/user/client can use the information</span>

The main things to mention are:

-   The measurement result, together with the uncertainty

-   The statement of the coverage factor and the level of confidence:

    $$ \ell = 21.49 \pm 0.05\, \mathrm{mm} $$ 


    The reported uncertainty is based on a standard uncertainty multiplied by coverage factor $k=2$, providing a level of confidence of approximately 95%, assuming normality.

## An example 1/2

<img src="fig/uncertainty_budget.png" alt="image" />

Source: https://www.muelaner.com/uncertainty-budget

## An example, 2/2

<img src="fig/combined_uncertainty.png" alt="image" />

Source: https://www.muelaner.com/uncertainty-budget/


## Eight steps to get the correct measurement

<img src="fig/8steps.png" alt="image" />

##  This is just the simplest case 

This is a simple example, we do not deal with special cases where different rules apply such as:

-   Small number of repeated readings - "Student's $t$ distribution

-   If one aspect of uncertainty dominates the calculation

-   If the inputs to the calculation are correlated

## Combination of uncertainties

-   We measured *N* physical quantities (variables),
    $x_1,x_2, \ldots, x_n$ (voltage,
    resistance, power, torque, length), each has its own uncertainty, $u_{x_i}$ (component uncertainty):

    $$x_{i} = \overline{x_{i}} + u_{x_{i}} $$

-   We want to estimate uncertainty of the result $y$ that depends on the measured ones:
    $$ y = f(x_1, x_2, \ldots, x_N) $$
    

-   We need to estimate $u_y$, using $u_{x_i}$ to obtain:
    $$ y = \overline{y} \pm u_{y} $$

-   **Two** **types**: <span style="color:red">maximum</span> (worst case) or <span style="color:red">expected</span> (probabilistic)

## Theory of uncertainty analysis Taylor expansion

$$ y + u_y = f(x_1+u_{x_1}, x_2 + u_{x_2} + \ldots) = $$

$$ = f(x_1, x_2 , ...) + \frac{\partial f}{\partial x_1} u_{x_1} +  \frac{\partial f}{\partial x_2} u_{x_2} + ...  + $$

$$+ \frac{1}{2} \left( (u_{x_1})^2 \frac{\partial^2 f}{\partial x_1^2} +  ...   \right) $$

## Maximum uncertainty

$$ u_{y,\mathrm{max}}=\sum_{i=1}^{i=N}\left| u_{x_{i}}\frac{\partial y}{\partial x_{i}} \right| $$

-   We assume that all the errors in the component measurements will **ADD** to the uncertainty of $y$, i.e. will be always of the same sign.

-   This is worst case scenario, unlikely for large number of variables (large *N*), but happens when we have a direct effect or a bias error (broken ruler, wrong diameter of spheres in cone measurements, lab A)

## Expected uncertainty

Root of the sum of squared uncertainty, RSS:

$$u_{R,\mathrm{RSS}}=\sqrt{\sum_{i=1}^{i=N}\left(u_{x_{i}}\frac{\partial R}{\partial x_{i}}\right)^{2}}$$

-   More realistic for large number of variables or for very different
    variables (using different instruments, randomization)

-   ISO standard if not stated otherwise:
    *u*<sub>*R*</sub> = *u*<sub>*R*, RSS</sub>

-   We known that $R=\overline{R}+u_{R}$ at the same confidence level
    as the components, typically 95% confidence level

-   Use dimensionless *u*<sub>*R*</sub>/*R*

Detailed example Measure volume flow rate, *Q* using the “bucket”
method, measure the time it takes to fill some volume ∀
*Q* = ∀/*t*

-   Measured: ∀ = 1.15 ± 0.05 liter, *t* = 33.0 ± 0.1 sec, both with 95%
    confidence

-   *Q* = ∀/*t* = 1.15/33.0(60 s/min) = 2.0909 ⇒ 2.09 liter/min (lpm)
    (note 3 sig. dig.)

-   Partial derivatives: ∂*Q*/∂∀ = 1/*t*,
    ∂*Q*/∂*t* =  − ∀/*t*<sup>2</sup>

-   *R* = *Q*, *u*<sub>∀</sub> = 0.05 liter, *u*<sub>*t*</sub> = 0.1
    sec.

The maximum, worst case method

$$u_{R,max}=\left|u_{\forall}\frac{\partial Q}{\partial \forall } \right|+\left|u_{t}\frac{\partial Q}{\partial t}\right| =$$

$$= u_{\forall}\frac{1}{t}+u_{t}\frac{\forall}{t^{2}}=$$

$$0.05\times\frac{1}{33.0}+0.1\times\frac{1.15}{33.0^{2}}=$$

 = 0.00162 × 60 = 0.0972 *l**p**m*

### The expectation method

$$u_{R,\textrm{RSS}}=\sqrt{\left(u_{\forall}\frac{\partial Q}{\partial\forall}\right)^{2}+\left(u_{t}\frac{\partial Q}{\partial t}\right)^{2}}=$$

$$= \sqrt{\left(u_{\forall}\frac{1}{t}\right)^{2}+\left(u_{t}\frac{\forall}{t^{2}}\right)^{2}}=$$

$$=\sqrt{\left(0.05\times\frac{1}{33.0}\right)^{2}+\left(0.1\times\frac{-1.15}{33.0^{2}}\right)^{2}}=$$

 = 0.00152 × 60 = 0.0911 *l**p**m*

The full and correct answer is *Q* = 2.09 ± 0.0911 lpm (with 95%
confidence)

What do we learn from the analysis ?

The **contribution of each variable to the overall uncertainty**:

-   *u*<sub>∀</sub>/∀ = 0.05/1.15 = 4.35%

-   *u*<sub>*t*</sub>/*t* = 0.1/33.0 = 0.303%

-   *u*<sub>*Q*</sub>/*Q* = 0.0911/2.09 = 4.35%

-   If we want to improve the result, which measurement shall we improve
    first?

Continued ...

-   For instance, improving the time accuracy and reducing it
    uncertainty by the factor of two will not affect the result at all.

-   Instead, improving volume by the factor of two ∀ = 1.150 + 0.025
    liters will cause *Q* = 2.09 ± 0.046 lpm - significant improvement.

Last example, how to save money for your startup

-   Shaft rotation speed measured by stroboscope with many repetitions.
    $\overline{N}=1734.2$ rpm, *S*<sub>*N*</sub> = 1.45 rpm.

-   Strobe accuracy by manufacturer  ± 1.00 rpm

-   *u*<sub>measurement</sub> =  ± 2*σ* =  ± 2.90 rpm (95%)
    *u*<sub>instrument</sub> =  ± 1.00 rpm

-   $u_{N}=\sqrt{u_{\textrm{meas.}}^{2}+u_{\textrm{instr.}}^{2}}=\sqrt{2.90^{2}+1.00^{2}}=3.068$
    rpm

-   The final result is:
    *N* = 1734.2 ± 3.07 rpm(95%*c*.*l*.)

-   The uncertainty is due to **the measurement uncertainty**, thus a
    more expensive tool will not help.
