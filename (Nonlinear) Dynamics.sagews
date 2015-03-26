︠d7436dbe-81bf-4ff5-9872-8839844313cci︠
%html
<center>
<h1>(Nonlinear) Dynamics</h1>
Adam Getchell
<br>
<img src="Lorenz-attractor.png">

</center>

<h2>Motivation</h2>
Why do we care about nonlinear systems? Well, first of all, because we can draw pretty pictures with fractals which captures public interest:
<p>
<center>
<img src="mandelbrot_set_1.jpg">
<p>
<img src="water-lilies.jpg">
<p>
<img src="choascope.jpg">
</center>
<p>
You can <a href="http://www.google.com/search?&q=fractals&ie=UTF-8&oe=UTF-8">Google</a> for <a href="http://images.google.com/images?client=safari&rls=en-us&q=fractals&ie=UTF-8&oe=UTF-8&um=1&sa=X&oi=image_result_group&resnum=1&ct=title">many</a>, <a href="http://sprott.physics.wisc.edu/fractals.htm">many</a> more <a href="http://en.wikipedia.org/wiki/Image:Mandel_zoom_00_mandelbrot_set.jpg">examples</a>, and there are tons of <a href="http://www.google.com/search?rls=en-us&q=fractal+software&ie=UTF-8&oe=UTF-8">software packages</a> dedicated just to creating beautiful images with fractals.
<p>
More importantly, many, many natural phenomena of interest occur that are essentially non-linear. In the linear world, you can break the system down into composite parts, solve each part separately, and then recombine the solutions to get the final answer.
<p>
(Un)Fortunately, the universe is quite a bit more complicated. Although we have made great progress in science using simplified models with linear properties, to understand more we need a new kind of ... we need extend our current toolset a bit, and incorporate all the advances of the past into a cohesive approach.
<p>
<b>Dynamics</b>, then, is the study of systems that change and evolve in time.
<p>
There are two types of dynamical systems: <i>differential equations</i> in continuous time and <i>iterated maps</i> (aka difference equations) in discrete time. When we solve them, often we know solutions for a particular set of initial conditions. We can then construct an abstract phase space describing the possible solution trajectories of the system. The goal of dynamics is to do the reverse: from the system, draw the trajectories from the phase space. This kind of geometric reasoning will often give good information about the solutions <i>without actually solving the system</i>!
<p>
A trick: most physical systems of interest have a time component. But by parametrizing time (set $x_{n+1} = t$ such that $\frac{dx_{n+1}}{dt} = 1$) we can turn an n-dimensional time-dependent system into an (n+1)-dimensional time independent system. (But don't tell the GR-string theory-quantum gravity crowd ;-)
<p>
<table border="2" bordercolor="" width="90%" bgcolor="" align=center>
<tr>
<td colspan=3 align=center>Dynamics - A Capsule History (Table 1.1.1 from Strogatz, Steven H. <i>Nonlinear Dynamics and Chaos: With Applications to Physics, Biology</i>) </td>
</tr>
<tr>
<td align=left>1666</td>
<td align=center>Newton</td>
<td align=center>Invention of calculus, explanation of planetary motion</td>
</tr>
<tr>
<td align=left>1700s</td>
<td align=center></td>
<td align=center>Flowering of calculus and classical mechanics</td>
</tr>
<tr>
<td align=left>1800s</td>
<td align=center></td>
<td align=center>Analytical studies of planetary motion</td>
</tr>
<tr>
<td align=left>1890s</td>
<td align=center>Poincare</td>
<td align=center>Geometric approach, nightmares of chaos</td>
</tr>
<tr>
<td align=left>1920-1950</td>
<td align=center></td>
<td align=center>Nonlinear oscillators in physics and engineering, invention of radio, radar, laser</td>
</tr>
<tr>
<td align=left>1920-1960</td>
<td align=center>Birkhoff<br>Kolmogorov<br>Arnol'd<br>Moser</td>
<td align=center>Complex behavior in Hamiltonian mechanics</td>
</tr>
<tr>
<td align=left>1963</td>
<td align=center>Lorenz</td>
<td align=center>Strange attractor in simple model of convection</td>
</tr>
<tr>
<td align=left>1970s</td>
<td align=center>Ruelle & Takens<br>May<br>Fiegenbaum<p>Winfree<br>Mandelbrot</td>
<td align=center>Turbulence and chaos<br>Chaos in logistic map<br>Universality and renormalization, connection between chaos and phase transitions<br>Experimental studies of chaos<br>Nonlinear oscillators in biology<br>Fractals</td>
</tr>
<tr>
<td align=left>1980s</td>
<td align=center></td>
<td align=center>Widespread interest in chaos, fractals, oscillators, and their applications</td>
</tr>
</table>

<h2>Introduction</h2>

A major technique in the analysis of nonlinear systems is the use of pictures. The basic idea is to recast a differential equation as a vector field. This often gives insight into systems for which no closed-form solution exists.
<p>
Consider the following equation:
$$
\large
\frac{dx}{dt} = \sin(x)
$$
First, note that this equation is exactly solvable. Many systems of interest do not have closed form solutions. Anyway, by separating variables we get:
$$
\large
dt = \frac{dx}{\sin(x)}
$$
Sage can solve this very quickly:

︡4680ce2f-a1f1-415e-8249-063583102542︡{"html": "<center>\r\n<h1>(Nonlinear) Dynamics</h1>\r\nAdam Getchell\r\n<br>\r\n<img src=\"Lorenz-attractor.png\">\r\n\r\n</center>\r\n\r\n<h2>Motivation</h2>\r\nWhy do we care about nonlinear systems? Well, first of all, because we can draw pretty pictures with fractals which captures public interest:\r\n<p>\r\n<center>\r\n<img src=\"mandelbrot_set_1.jpg\">\r\n<p>\r\n<img src=\"water-lilies.jpg\">\r\n<p>\r\n<img src=\"choascope.jpg\">\r\n</center>\r\n<p>\r\nYou can <a href=\"http://www.google.com/search?&q=fractals&ie=UTF-8&oe=UTF-8\">Google</a> for <a href=\"http://images.google.com/images?client=safari&rls=en-us&q=fractals&ie=UTF-8&oe=UTF-8&um=1&sa=X&oi=image_result_group&resnum=1&ct=title\">many</a>, <a href=\"http://sprott.physics.wisc.edu/fractals.htm\">many</a> more <a href=\"http://en.wikipedia.org/wiki/Image:Mandel_zoom_00_mandelbrot_set.jpg\">examples</a>, and there are tons of <a href=\"http://www.google.com/search?rls=en-us&q=fractal+software&ie=UTF-8&oe=UTF-8\">software packages</a> dedicated just to creating beautiful images with fractals.\r\n<p>\r\nMore importantly, many, many natural phenomena of interest occur that are essentially non-linear. In the linear world, you can break the system down into composite parts, solve each part separately, and then recombine the solutions to get the final answer.\r\n<p>\r\n(Un)Fortunately, the universe is quite a bit more complicated. Although we have made great progress in science using simplified models with linear properties, to understand more we need a new kind of ... we need extend our current toolset a bit, and incorporate all the advances of the past into a cohesive approach.\r\n<p>\r\n<b>Dynamics</b>, then, is the study of systems that change and evolve in time.\r\n<p>\r\nThere are two types of dynamical systems: <i>differential equations</i> in continuous time and <i>iterated maps</i> (aka difference equations) in discrete time. When we solve them, often we know solutions for a particular set of initial conditions. We can then construct an abstract phase space describing the possible solution trajectories of the system. The goal of dynamics is to do the reverse: from the system, draw the trajectories from the phase space. This kind of geometric reasoning will often give good information about the solutions <i>without actually solving the system</i>!\r\n<p>\r\nA trick: most physical systems of interest have a time component. But by parametrizing time (set $x_{n+1} = t$ such that $\\frac{dx_{n+1}}{dt} = 1$) we can turn an n-dimensional time-dependent system into an (n+1)-dimensional time independent system. (But don't tell the GR-string theory-quantum gravity crowd ;-)\r\n<p>\r\n<table border=\"2\" bordercolor=\"\" width=\"90%\" bgcolor=\"\" align=center>\r\n<tr>\r\n<td colspan=3 align=center>Dynamics - A Capsule History (Table 1.1.1 from Strogatz, Steven H. <i>Nonlinear Dynamics and Chaos: With Applications to Physics, Biology</i>) </td>\r\n</tr>\r\n<tr>\r\n<td align=left>1666</td>\r\n<td align=center>Newton</td>\r\n<td align=center>Invention of calculus, explanation of planetary motion</td>\r\n</tr>\r\n<tr>\r\n<td align=left>1700s</td>\r\n<td align=center></td>\r\n<td align=center>Flowering of calculus and classical mechanics</td>\r\n</tr>\r\n<tr>\r\n<td align=left>1800s</td>\r\n<td align=center></td>\r\n<td align=center>Analytical studies of planetary motion</td>\r\n</tr>\r\n<tr>\r\n<td align=left>1890s</td>\r\n<td align=center>Poincare</td>\r\n<td align=center>Geometric approach, nightmares of chaos</td>\r\n</tr>\r\n<tr>\r\n<td align=left>1920-1950</td>\r\n<td align=center></td>\r\n<td align=center>Nonlinear oscillators in physics and engineering, invention of radio, radar, laser</td>\r\n</tr>\r\n<tr>\r\n<td align=left>1920-1960</td>\r\n<td align=center>Birkhoff<br>Kolmogorov<br>Arnol'd<br>Moser</td>\r\n<td align=center>Complex behavior in Hamiltonian mechanics</td>\r\n</tr>\r\n<tr>\r\n<td align=left>1963</td>\r\n<td align=center>Lorenz</td>\r\n<td align=center>Strange attractor in simple model of convection</td>\r\n</tr>\r\n<tr>\r\n<td align=left>1970s</td>\r\n<td align=center>Ruelle & Takens<br>May<br>Fiegenbaum<p>Winfree<br>Mandelbrot</td>\r\n<td align=center>Turbulence and chaos<br>Chaos in logistic map<br>Universality and renormalization, connection between chaos and phase transitions<br>Experimental studies of chaos<br>Nonlinear oscillators in biology<br>Fractals</td>\r\n</tr>\r\n<tr>\r\n<td align=left>1980s</td>\r\n<td align=center></td>\r\n<td align=center>Widespread interest in chaos, fractals, oscillators, and their applications</td>\r\n</tr>\r\n</table>\r\n\r\n<h2>Introduction</h2>\r\n\r\nA major technique in the analysis of nonlinear systems is the use of pictures. The basic idea is to recast a differential equation as a vector field. This often gives insight into systems for which no closed-form solution exists.\r\n<p>\r\nConsider the following equation:\r\n$$\r\n\\large\r\n\\frac{dx}{dt} = \\sin(x)\r\n$$\r\nFirst, note that this equation is exactly solvable. Many systems of interest do not have closed form solutions. Anyway, by separating variables we get:\r\n$$\r\n\\large\r\ndt = \\frac{dx}{\\sin(x)}\r\n$$\r\nSage can solve this very quickly:"}︡
︠038a659e-55d6-4938-860f-4776b78aab20︠
integral(csc(x),x)
︡c4158460-74cd-4857-a00e-07a2f788dd80︡{"stdout": "-log(csc(x) + cot(x))"}︡
︠01cf6872-09c9-4b69-8b82-9f06908ceb22i︠
%html
<p>
Now, this is an <i>indefinite</i> integral, which means the actual solution is:
$$
\large
t = -\log|\csc(x) +\cot(x)| + C
$$
We have to find the constant C by the usual means, let $x = x_0 @ t = 0$. Then $C = log|csc(x_0) + cot(x_0)|$, and the full solution is:
$$
\large
t = \log|\frac{\csc(x_0) + \cot(x_0)}{(\csc(x) + \cot(x)}|
$$
But what does this mean exactly?
<p>
Quick, if $x_0=\pi/4$, what happens as $t\rightarrow\infty$? What happens as $t\rightarrow\infty$ for arbitrary $x_0$?
<p>
Let's think about this another way.
<p>
Instead, let's plot $\frac{dx}{dt}$ versus x, and think of the function as a vector field with fluid flowing steadily along the x-axis with velocity that varies according to the rule $\frac{dx}{dt} = \sin(x)$.

︡d56caa50-5149-4c70-90cb-445ef5b7675e︡{"html": "<p>\r\nNow, this is an <i>indefinite</i> integral, which means the actual solution is:\r\n$$\r\n\\large\r\nt = -\\log|\\csc(x) +\\cot(x)| + C\r\n$$\r\nWe have to find the constant C by the usual means, let $x = x_0 @ t = 0$. Then $C = log|csc(x_0) + cot(x_0)|$, and the full solution is:\r\n$$\r\n\\large\r\nt = \\log|\\frac{\\csc(x_0) + \\cot(x_0)}{(\\csc(x) + \\cot(x)}|\r\n$$\r\nBut what does this mean exactly?\r\n<p>\r\nQuick, if $x_0=\\pi/4$, what happens as $t\\rightarrow\\infty$? What happens as $t\\rightarrow\\infty$ for arbitrary $x_0$?\r\n<p>\r\nLet's think about this another way.\r\n<p>\r\nInstead, let's plot $\\frac{dx}{dt}$ versus x, and think of the function as a vector field with fluid flowing steadily along the x-axis with velocity that varies according to the rule $\\frac{dx}{dt} = \\sin(x)$."}︡
︠7ae00f45-96c2-4a3b-a283-d1ff4b232c57︠
''' Plot vector field picture of f
    Later, this should calculate arrows from zeroes of f automatically
'''

plotrange = 3
x = var('x')
f = sin(x)

# Add plot
g = plot(f, -plotrange * pi, plotrange * pi)

# Add arrows
startx = []
endx = []
arrow_len = 1
    
def create_arrow_endpoints(start, end, arrow_length, n, parity):
    if parity:
        start.append(n*pi - arrow_length)
        start.append(n*pi + arrow_length)
        end.append(n*pi)
        end.append(n*pi)
    else:
        start.append(n * pi)
        start.append(n * pi)
        end.append(n*pi - arrow_length)
        end.append(n*pi + arrow_length)

for i in range(-plotrange, plotrange+1):
    odd = (True if i % 2 != 0 else False)
    create_arrow_endpoints(startx, endx, arrow_len, i, odd)

y = [0 for y in range(len(startx))]
arrowstart = zip(startx, y)
arrowend = zip(endx, y)

def arrow_gen(start, stop):
    ''' Creates an arrow starting at start and ending at stop
        with color and line width
    '''
    return arrow(start, stop, rgbcolor=(1,0,0), width=0.05)

for i in range(len(arrowstart)):
    g += arrow_gen(arrowstart.pop(), arrowend.pop())

g.show()
︡a70d006a-dc92-4651-bf58-cefb3dfc1cbb︡{"html": "<font color='black'><img src='cell://sage0.png'></font>"}︡
︠96356d99-975a-4cda-a524-666330ae6efbi︠
%html
<p>
When $\frac{dx}{dt}$ is positive, flow is to the right (+x direction). When $\frac{dx}{dt}$ is negative, flow is to the left (-x direction). Where $\frac{dx}{dt}$ is zero, there is no flow, and these are called <b>fixed points</b>. Notice that the fixed points can be classified in terms of their stability:
<p>
<ul>
<li><B>Stable fixed points</B> (attractors)</li>
<li><B>Unstable fixed points</B> (repellors)</li>
<li><B>Saddle points</B></li>
</ul>
<p>
This classification carries over to higher-dimensional systems, with additions. For now, note that stability is a local property only; if you perturb the system far enough, you will get different behavior.
<p>
If we plot the actual solution to the equation (now x is the x-axis, t is the y-axis), we get:
<p>

︡50c7ef1e-5e2f-4811-8f8f-5530eaa2bd28︡{"html": "<p>\r\nWhen $\\frac{dx}{dt}$ is positive, flow is to the right (+x direction). When $\\frac{dx}{dt}$ is negative, flow is to the left (-x direction). Where $\\frac{dx}{dt}$ is zero, there is no flow, and these are called <b>fixed points</b>. Notice that the fixed points can be classified in terms of their stability:\r\n<p>\r\n<ul>\r\n<li><B>Stable fixed points</B> (attractors)</li>\r\n<li><B>Unstable fixed points</B> (repellors)</li>\r\n<li><B>Saddle points</B></li>\r\n</ul>\r\n<p>\r\nThis classification carries over to higher-dimensional systems, with additions. For now, note that stability is a local property only; if you perturb the system far enough, you will get different behavior.\r\n<p>\r\nIf we plot the actual solution to the equation (now x is the x-axis, t is the y-axis), we get:\r\n<p>"}︡
︠3d1608f5-73ef-4169-baa0-a651ce5f7a37︠
@interact
def f(c = slider(-10, 10, .25, label = 'x0')):
    print c
    show(plot(log(abs((((csc(c)+cot(c))/(csc(x)+cot(x))))))))
︡879c8b38-de0a-4f0c-91eb-1fff254ea606︡{"html": "<!--notruncate-->\n        <div padding=6 id=\"div-interact-3\">\n          <table width=800px height=20px bgcolor=\"#c5c5c5\" cellpadding=15>\n            <tr>\n              <td bgcolor=\"#f9f9f9\" valign=top align=left>\n            <table>\n              <tr><td colspan=3><table><tr><td align=right><font color=\"black\">x0&nbsp;</font></td><td>\n        <table>\n          <tr>\n            <td>\n              <div id=\"slider-c-3\" style=\"margin:0px; margin-left: 1.0em; margin-right: 1.0em; width: 15.0em;\"></div>\n            </td>\n            \n            <td>\n              <font color=\"black\" id=\"slider-c-3-lbl\"></font>\n            </td>\n          </tr>\n        </table><script>\n    (function() {\n        var values = [\"-10.0000000000000\",\"-9.75000000000000\",\"-9.50000000000000\",\"-9.25000000000000\",\"-9.00000000000000\",\"-8.75000000000000\",\"-8.50000000000000\",\"-8.25000000000000\",\"-8.00000000000000\",\"-7.75000000000000\",\"-7.50000000000000\",\"-7.25000000000000\",\"-7.00000000000000\",\"-6.75000000000000\",\"-6.50000000000000\",\"-6.25000000000000\",\"-6.00000000000000\",\"-5.75000000000000\",\"-5.50000000000000\",\"-5.25000000000000\",\"-5.00000000000000\",\"-4.75000000000000\",\"-4.50000000000000\",\"-4.25000000000000\",\"-4.00000000000000\",\"-3.75000000000000\",\"-3.50000000000000\",\"-3.25000000000000\",\"-3.00000000000000\",\"-2.75000000000000\",\"-2.50000000000000\",\"-2.25000000000000\",\"-2.00000000000000\",\"-1.75000000000000\",\"-1.50000000000000\",\"-1.25000000000000\",\"-1.00000000000000\",\"-0.750000000000000\",\"-0.500000000000000\",\"-0.250000000000000\",\"0.000000000000000\",\"0.250000000000000\",\"0.500000000000000\",\"0.750000000000000\",\"1.00000000000000\",\"1.25000000000000\",\"1.50000000000000\",\"1.75000000000000\",\"2.00000000000000\",\"2.25000000000000\",\"2.50000000000000\",\"2.75000000000000\",\"3.00000000000000\",\"3.25000000000000\",\"3.50000000000000\",\"3.75000000000000\",\"4.00000000000000\",\"4.25000000000000\",\"4.50000000000000\",\"4.75000000000000\",\"5.00000000000000\",\"5.25000000000000\",\"5.50000000000000\",\"5.75000000000000\",\"6.00000000000000\",\"6.25000000000000\",\"6.50000000000000\",\"6.75000000000000\",\"7.00000000000000\",\"7.25000000000000\",\"7.50000000000000\",\"7.75000000000000\",\"8.00000000000000\",\"8.25000000000000\",\"8.50000000000000\",\"8.75000000000000\",\"9.00000000000000\",\"9.25000000000000\",\"9.50000000000000\",\"9.75000000000000\",\"10.0000000000000\"];\n        setTimeout(function() {\n            $('#slider-c-3').slider({\n                step: 1,\n                min: 0,\n                max: 80,\n                value: 0,\n                change: function (e, ui) {\n                    var position = ui.value;\n                    if (values != null) {\n                        $('#slider-c-3-lbl').text(values[position]);\n                        interact(3, {variable: 'c', adapt_number: 1, value: encode64(position)}, 1);\n                    }\n                },\n                slide: function (e, ui) {\n                    if (values != null) {\n                        $('#slider-c-3-lbl').text(values[ui.value]);\n                    }\n                }\n            });\n            if (values != null) {\n                $('#slider-c-3-lbl').text(values[$('#slider-c-3').slider('value')]);\n            }\n        }, 1);\n    })();\n    </script></td>\n</tr></table></td></tr>\n              <tr><td></td><td style='width: 100%;'>\n        <div id=\"cell-interact-3\"><?__SAGE__START>\n          <table border=0 bgcolor=\"white\" width=100%>\n            <tr>\n              <td bgcolor=\"white\" align=left valign=top>\n                <pre><?__SAGE__TEXT></pre>\n              </td>\n            </tr>\n            <tr>\n              <td align=left valign=top><?__SAGE__HTML></td>\n            </tr>\n          </table><?__SAGE__END>\n        </div></td><td></td></tr>\n              <tr><td colspan=3></td></tr>\n            </table></td>\n            </tr>\n          </table>\n        </div>"}︡
︠17b349b9-f00d-45d8-b705-3929d9360db6i︠
%html
<p>
Inspecting this, just like in the previous diagram we can see that for $\frac{\pi}{4}$ the system tends to accelerate at first towards the right, but then slow down as it approaches a limiting value. Of course, often times we don't have the luxury of an exact equation to plot! 
<p>
In the previous case, we found the <b>fixed points</b> of the system, which helped us identify the behavior of the equation for various domains of interest. Next, we'll consider adding a parameter <b>r</b> to the system. We'll start off with a simple equation, $y = x^2 + r$:
<p>

︡587ff70e-0feb-4b0c-aa38-04bf8d7081fb︡{"html": "<p>\r\nInspecting this, just like in the previous diagram we can see that for $\\frac{\\pi}{4}$ the system tends to accelerate at first towards the right, but then slow down as it approaches a limiting value. Of course, often times we don't have the luxury of an exact equation to plot! \r\n<p>\r\nIn the previous case, we found the <b>fixed points</b> of the system, which helped us identify the behavior of the equation for various domains of interest. Next, we'll consider adding a parameter <b>r</b> to the system. We'll start off with a simple equation, $y = x^2 + r$:\r\n<p>"}︡
︠0b7747cb-2335-49a1-8bda-f3a8c5910d3d︠
@interact
def f(r = slider(-3,3,.25, label = 'r')):
    show(plot(r + x**2, -3, 3))
︡0870ff61-2881-4e4c-81fd-ff74556037d7︡{"html": "<!--notruncate-->\n        <div padding=6 id=\"div-interact-4\">\n          <table width=800px height=20px bgcolor=\"#c5c5c5\" cellpadding=15>\n            <tr>\n              <td bgcolor=\"#f9f9f9\" valign=top align=left>\n            <table>\n              <tr><td colspan=3><table><tr><td align=right><font color=\"black\">r&nbsp;</font></td><td>\n        <table>\n          <tr>\n            <td>\n              <div id=\"slider-r-4\" style=\"margin:0px; margin-left: 1.0em; margin-right: 1.0em; width: 15.0em;\"></div>\n            </td>\n            \n            <td>\n              <font color=\"black\" id=\"slider-r-4-lbl\"></font>\n            </td>\n          </tr>\n        </table><script>\n    (function() {\n        var values = [\"-3.00000000000000\",\"-2.75000000000000\",\"-2.50000000000000\",\"-2.25000000000000\",\"-2.00000000000000\",\"-1.75000000000000\",\"-1.50000000000000\",\"-1.25000000000000\",\"-1.00000000000000\",\"-0.750000000000000\",\"-0.500000000000000\",\"-0.250000000000000\",\"0.000000000000000\",\"0.250000000000000\",\"0.500000000000000\",\"0.750000000000000\",\"1.00000000000000\",\"1.25000000000000\",\"1.50000000000000\",\"1.75000000000000\",\"2.00000000000000\",\"2.25000000000000\",\"2.50000000000000\",\"2.75000000000000\",\"3.00000000000000\"];\n        setTimeout(function() {\n            $('#slider-r-4').slider({\n                step: 1,\n                min: 0,\n                max: 24,\n                value: 0,\n                change: function (e, ui) {\n                    var position = ui.value;\n                    if (values != null) {\n                        $('#slider-r-4-lbl').text(values[position]);\n                        interact(4, {variable: 'r', adapt_number: 2, value: encode64(position)}, 1);\n                    }\n                },\n                slide: function (e, ui) {\n                    if (values != null) {\n                        $('#slider-r-4-lbl').text(values[ui.value]);\n                    }\n                }\n            });\n            if (values != null) {\n                $('#slider-r-4-lbl').text(values[$('#slider-r-4').slider('value')]);\n            }\n        }, 1);\n    })();\n    </script></td>\n</tr></table></td></tr>\n              <tr><td></td><td style='width: 100%;'>\n        <div id=\"cell-interact-4\"><?__SAGE__START>\n          <table border=0 bgcolor=\"white\" width=100%>\n            <tr>\n              <td bgcolor=\"white\" align=left valign=top>\n                <pre><?__SAGE__TEXT></pre>\n              </td>\n            </tr>\n            <tr>\n              <td align=left valign=top><?__SAGE__HTML></td>\n            </tr>\n          </table><?__SAGE__END>\n        </div></td><td></td></tr>\n              <tr><td colspan=3></td></tr>\n            </table></td>\n            </tr>\n          </table>\n        </div>"}︡
︠bd290e38-456b-464c-839c-7d00b2d41a84i︠
%html
<p>
Notice that the location and classification of our fixed points depends upon the value of r.
</p>
Now let's look at a deceptively simple equation, the Logistic equation:
$$
\large
y = r*x*(1-x)
$$
<p>

︡cfb7672b-e755-4cbb-88fa-4e29572eab6d︡{"html": "<p>\r\nNotice that the location and classification of our fixed points depends upon the value of r.\r\n</p>\r\nNow let's look at a deceptively simple equation, the Logistic equation:\r\n$$\r\n\\large\r\ny = r*x*(1-x)\r\n$$\r\n<p>"}︡
︠9d7fc58c-d10b-442d-9382-afa86cb4cab3︠
@interact
def f(r = slider(0, 5,.1, label='r')):
    show(plot(r * x * (1.0 - x), 3, -3))
︡e4c3fc51-31ea-49d5-873a-9665ae30da5b︡︡
︠b39b260d-3f1e-4a66-afd0-0715c6067d88i︠
%html
<p>
Something strange is going on here; we are getting different values. One tool we can use to look at its stability is a CobWeb diagram.
<p>

︡9322b014-b80d-4169-ae42-1cfa1a049696︡{"html": "<p>\r\nSomething strange is going on here; we are getting different values. One tool we can use to look at its stability is a CobWeb diagram.\r\n<p>"}︡
︠96aa2f7a-b76e-4c0c-8bde-b6216b75edaai︠
%hide
# LogisticCobweb.py:
#    Plot the Logistic Map's quadratic function
#   And show iterating from an initial condition

# Import modules
from numpy import *
# Plotting
from pylab import *

# Define the Logistic map's function 
def LogisticMap(r,x):
    return r * x * (1.0 - x)

# Setup x array
# Note how we make sure x = 1.0 is included
x = arange(0.0,1.01,0.01)
# We set r = 3.678, where two bands merge to one
r = 3.678
# Set the initial condition
state = 0.5

# Setup the plot
# It's numbered 1 and is 6 x 6 inches, to make the plot square.
# On my display this didn't turn out to be square, so I've fudged.
figure(1,(6,5.8))
# Note how we turn the parameter value into a string
#   using the string formating commands.
TitleString = 'Logistic map: f(x) = r*x*(1 - x) for r = %g and x0 = %g' % (r, state)
title(TitleString)
xlabel('X(n)')   # set x-axis label
ylabel('X(n+1)') # set y-axis label

# We plot the identity y = x for reference
plot(x, x, 'b--', antialiased=True)

# Here's the Logistic Map itself
plot(x, LogisticMap(r,x), 'g', antialiased=True)

# ... and its second iterate

# Establish the arrays to hold the line end points
x0 = [ ] # The x_n value
x1 = [ ] # The next value x_n+1
# Iterate for a few time steps
nIterates = 20
# Plot lines, showing how the iteration is reflected off of the identity
for n in xrange(nIterates):
    x0.append( state )
    x1.append( state )
    x0.append( state )
    state = LogisticMap(r,state)
    x1.append( state )

# Plot the lines all at once
plot(x0, x1, 'r', antialiased=True)
savefig('LogisticBifn0', dpi=100)

# Display plot in window
show()
︡7a09fe60-3e34-475d-a931-b9fb552052ab︡︡
︠6755367f-7deb-4403-9fad-b7f8fb67ee66i︠
%html
<p>
Now lets go onto 2D systems. Let's consider the system with the parameter a:
$$
\large
\frac{dx}{dt} = -y + ax(x^2+y^2)
$$
$$
\large
\frac{dy}{dt} = x + ay(x^2+y^2)
$$
<p>

︡68c27622-ab23-46b2-8b2d-42ce6c96da63︡{"html": "<p>\r\nNow lets go onto 2D systems. Let's consider the system with the parameter a:\r\n$$\r\n\\large\r\n\\frac{dx}{dt} = -y + ax(x^2+y^2)\r\n$$\r\n$$\r\n\\large\r\n\\frac{dy}{dt} = x + ay(x^2+y^2)\r\n$$\r\n<p>"}︡
︠f9a79f4c-63e1-4c6b-abb3-dc1ba77bcc49︠
a=-1
plot_vector_field((lambda x,y:-y+a*x*(x^2+y^2),lambda x,y:x+a*y*(x^2+y^2)), (x,-3,3),(y,-3,3))
︡42f4e729-a30b-4ba6-b0de-4a9f441ea659︡︡
︠7fcc6641-11fd-4273-a6be-598ae8b5c0dfi︠
%html
<p>
Bifurcation and Period doubling
<p>

︡3a04453e-4647-4069-86a5-05e0b4efe6b5︡{"html": "<p>\r\nBifurcation and Period doubling\r\n<p>"}︡
︠3a309e12-4927-47a4-a755-2b2df5fcd965︠
%cython

'''Plot a bifurcation diagram for the Logistic Map
    x_n+1 = r*x_n*(1 - x_n)
'''

from numpy import *
from pylab import *
import math

# Define LogisticMap

def LogisticMap(double r, double x):
    #return r * x * (1.0 - x)
    return r * x - x*x*x

# Setup parameter range
rlow  = 1
rhigh = 4.0

# Setup the plot
# Stuff parameter range into a string via the string formating commands.
TitleString  = 'Logistic map, f(x) = r*x*(1 - x), '
TitleString += 'bifurcation diagram for r in [%g,%g]' % (rlow,rhigh)
title(TitleString)
# Label axes
xlabel('Control parameter r')
ylabel('{X(n)}')
# Set the initial condition used across the different parameters
ic = .01
# Establish the arrays to hold the set of iterates at each parameter value
# The iterates we'll throw away
nTransients = 200
# This sets how much the attractor is filled in
nIterates = 250
# This sets how dense the bifurcation diagram will be
nSteps = 500
# Sweep the control parameter over the desired range
rInc = (rhigh-rlow)/float(nSteps)
for r in arange(rlow,rhigh,rInc):
    # Set the initial condition to the reference value
    state = ic
    # Throw away the transient iterations
    for i in xrange(nTransients):
        state = LogisticMap(r,state)
    # Now store the next batch of iterates
    rsweep = [ ]   # The parameter value
    x = [ ]        # The iterates
    for i in xrange(nIterates):
        state = LogisticMap(r,state)
        rsweep.append(r)
        x.append( state )
    plot(rsweep, x, 'k,') # Plot the list of (r,x) pairs as pixels

# Use this to save figure as a bitmap png file
savefig('LogisticBifn', dpi=100)

# Turn on matplotlib's interactive mode.
#ion()

# Display plot in window
show()
︡a5c2a8d8-6943-4ae5-b46e-b1301c07a602︡︡
︠51ecab36-22da-4dcb-994d-cd82dc5b2d15i︠
%html
<p>
Bifurcation for Cosine map
<p>
<h2>Universality</h2>
<p>
It's remarkable how similiar these two bifurcation plots look, even for systems with quite different character. The resemblance is more than skin deep. Due to a 1973 theorem by Metropolis et. al., the periodic attractors always occur in the same sequence! This sequence is called the U-sequence:
<p>
$$
\large
1, 2, 2x2, 6, 5, 3, 2x3, 5, 6, 4, 6, 5, 6 ...
$$
<p>
Thus, for systems in the low range of chaotic behavior, the form of $f(x)$ is irrelevant!
<p>
Furthermore, they all period-double at same rate! This rate is given by the Feigenbaum constant, $\delta = 4.699$.
<p>
Amazingly, regardless of the details of the physical system, they exhibit bifurcations (period-doubling) in the same order, at the same rate!

<p>
<h2>Chaos</h2>
<p>
Chaos is defined as <i>aperiodic long-term behavior</i> in a <i>deterministic</i> system that exhibits <i>sensitive dependence on initial conditions</i> (positive Liapunov exponent).
<p>
Chaos is not equivalent to instability. For example, $\frac{dx}{dt}=x$ is deterministic and shows separation of nearby trajectories. It's not chaotic because the trajectories are repelled to inifinity and never return. So $\infty$ acts like an attracting <i>fixed point</i>, whereas true chaotic behavior is aperiodic (which excludes fixed points as well as periodic behavior).
<p>
The canonical example is the <i>Lorenz equations</i>:
$$\frac{dx}{dt} = \sigma(y-x)
$$
$$\frac{dy}{dt} = rx - y -xz
$$
$$\frac{dz}{dt} = xy - bz
$$
<p>
In sum, there's a lot more we don't know about dynamical systems and chaos. Hopefully many of you will help find answers!
<p>
<table border="2" bordercolor="" width="90%" bgcolor="" align=center>
<tr>
<td colspan=6 align=center>Table 1.3.1 from Strogatz, Steven H. <i>Nonlinear Dynamics and Chaos: With Applications to Physics, Biology</i>) </td>
</tr>
<tr>
<td></td>
<td colspan=5 align=center>Number of variables $\rightarrow$</td>
<tr>
<td></td>
<td align=left>n=1</td>
<td align=center>n=2</td>
<td align=center>n>=3</td>
<td align=center>n>>1</td>
<td align=center>Continuum</td>
</tr>
<tr>
<td align=left rowspan=2>Linear</td>
<td align=center><i>Growth, decay, or equilibrium</i></td>
<td align=center><i>Oscillations</i></td>
<td></td>
<td align=center><i>Collective phenomena</i></td>
<td align=center><i>Wave and patterns</i></td>
</tr>
<tr>
<td align=center>Exponential growth<br>RC circuit<br>Radioactive decay</td>
<td align=center>Linear oscillators<br>Mass and spring<br>RLC circuit<br>2-body problem (Kepler, Newton)</td>
<td align=center>Civil engineering, structures<br>Electrical engineering</td>
<td align=center>Coupled harmonic oscillators<br>Solid-state physics<br>Molecular dynamics<br>Equilibrium statistical mechanics</td>
<td align=center>Elasticity<br>Wave equations<br>Electromagnetism (Maxwell)<br>Quantum mechanics (Schrodinger, Heisenberg, Direc)<br>Heat and diffusion<br>Acoustics<br>Viscous fluids</td>
</tr>
<tr>
<td align=left>Nonlinear</td>
<td align=center>Fixed points<br>Bifurcations<br>Overdamped systems, relaxational dynamics<br>Logistic equation for single species</td>
<td align=center>Pendulum<br>Anharmonic oscillators<br>Limit cycles<br>Biological oscillators (neurons, heart cells)<br>Predator-prey cycles<br>Nonlinear electronics (van der Pol, Josephson)</td>
<td align=center><i>Chaos</i><br>Strange attractors (Lorenz)<br>3-body problem (Poincare)<br>Chemical kinetics<br>Iterated maps (Feigenbaum)<br>Fractals (Mandelbrot)<br>Forced nonlinear oscillators (Levinson, Smale)<br>Practical uses of chaos<br>Quantum chaos?</td>
<td align=center>Coupled nonlinear oscillators<br>Lasers, nonlinear optics<br>Nonequilibrium statistical mechanics<br>Nonlinear solid-state physics (semiconductors)<br>Josephson arrays<br>Heart cell synchronization<br>Neural networks<br>Immune system<br>Ecosystems<br>Economics</td>
<td align=center><i>Spatio-temporal complexity</i><br>Nonlinear waves (shocks, solitons)<br>Plasmas<br>Earthquakes<br>General Relativity (Einstein)<br>Quantum field theory<br>Reaction-diffusion, biological and chemical waves<br>Fibrillation<br>Epilepsy<br>Turbulent fluids (Navier-Stokes)<br>Life
</tr>
</table>
<p>
Thanks to Professor James Crutchfield and his <a href="http://cse.ucdavis.edu/~chaos/courses/nlp/">PHY 250 Nonlinear Dynamics</a> class
<p>
<h2>References:</h2>
<p>
Strogatz, Steven H. <i>Nonlinear Dynamics and Chaos: With Applications to Physics, Biology</i>. Studies in Nonlinearity. Westview Press, 2001.
<p>

︡8647c9f9-78b8-40d3-a7e2-180036cc133f︡{"html": "<p>\r\nBifurcation for Cosine map\r\n<p>\r\n<h2>Universality</h2>\r\n<p>\r\nIt's remarkable how similiar these two bifurcation plots look, even for systems with quite different character. The resemblance is more than skin deep. Due to a 1973 theorem by Metropolis et. al., the periodic attractors always occur in the same sequence! This sequence is called the U-sequence:\r\n<p>\r\n$$\r\n\\large\r\n1, 2, 2x2, 6, 5, 3, 2x3, 5, 6, 4, 6, 5, 6 ...\r\n$$\r\n<p>\r\nThus, for systems in the low range of chaotic behavior, the form of $f(x)$ is irrelevant!\r\n<p>\r\nFurthermore, they all period-double at same rate! This rate is given by the Feigenbaum constant, $\\delta = 4.699$.\r\n<p>\r\nAmazingly, regardless of the details of the physical system, they exhibit bifurcations (period-doubling) in the same order, at the same rate!\r\n\r\n<p>\r\n<h2>Chaos</h2>\r\n<p>\r\nChaos is defined as <i>aperiodic long-term behavior</i> in a <i>deterministic</i> system that exhibits <i>sensitive dependence on initial conditions</i> (positive Liapunov exponent).\r\n<p>\r\nChaos is not equivalent to instability. For example, $\\frac{dx}{dt}=x$ is deterministic and shows separation of nearby trajectories. It's not chaotic because the trajectories are repelled to inifinity and never return. So $\\infty$ acts like an attracting <i>fixed point</i>, whereas true chaotic behavior is aperiodic (which excludes fixed points as well as periodic behavior).\r\n<p>\r\nThe canonical example is the <i>Lorenz equations</i>:\r\n$$\\frac{dx}{dt} = \\sigma(y-x)\r\n$$\r\n$$\\frac{dy}{dt} = rx - y -xz\r\n$$\r\n$$\\frac{dz}{dt} = xy - bz\r\n$$\r\n<p>\r\nIn sum, there's a lot more we don't know about dynamical systems and chaos. Hopefully many of you will help find answers!\r\n<p>\r\n<table border=\"2\" bordercolor=\"\" width=\"90%\" bgcolor=\"\" align=center>\r\n<tr>\r\n<td colspan=6 align=center>Table 1.3.1 from Strogatz, Steven H. <i>Nonlinear Dynamics and Chaos: With Applications to Physics, Biology</i>) </td>\r\n</tr>\r\n<tr>\r\n<td></td>\r\n<td colspan=5 align=center>Number of variables $\\rightarrow$</td>\r\n<tr>\r\n<td></td>\r\n<td align=left>n=1</td>\r\n<td align=center>n=2</td>\r\n<td align=center>n>=3</td>\r\n<td align=center>n>>1</td>\r\n<td align=center>Continuum</td>\r\n</tr>\r\n<tr>\r\n<td align=left rowspan=2>Linear</td>\r\n<td align=center><i>Growth, decay, or equilibrium</i></td>\r\n<td align=center><i>Oscillations</i></td>\r\n<td></td>\r\n<td align=center><i>Collective phenomena</i></td>\r\n<td align=center><i>Wave and patterns</i></td>\r\n</tr>\r\n<tr>\r\n<td align=center>Exponential growth<br>RC circuit<br>Radioactive decay</td>\r\n<td align=center>Linear oscillators<br>Mass and spring<br>RLC circuit<br>2-body problem (Kepler, Newton)</td>\r\n<td align=center>Civil engineering, structures<br>Electrical engineering</td>\r\n<td align=center>Coupled harmonic oscillators<br>Solid-state physics<br>Molecular dynamics<br>Equilibrium statistical mechanics</td>\r\n<td align=center>Elasticity<br>Wave equations<br>Electromagnetism (Maxwell)<br>Quantum mechanics (Schrodinger, Heisenberg, Direc)<br>Heat and diffusion<br>Acoustics<br>Viscous fluids</td>\r\n</tr>\r\n<tr>\r\n<td align=left>Nonlinear</td>\r\n<td align=center>Fixed points<br>Bifurcations<br>Overdamped systems, relaxational dynamics<br>Logistic equation for single species</td>\r\n<td align=center>Pendulum<br>Anharmonic oscillators<br>Limit cycles<br>Biological oscillators (neurons, heart cells)<br>Predator-prey cycles<br>Nonlinear electronics (van der Pol, Josephson)</td>\r\n<td align=center><i>Chaos</i><br>Strange attractors (Lorenz)<br>3-body problem (Poincare)<br>Chemical kinetics<br>Iterated maps (Feigenbaum)<br>Fractals (Mandelbrot)<br>Forced nonlinear oscillators (Levinson, Smale)<br>Practical uses of chaos<br>Quantum chaos?</td>\r\n<td align=center>Coupled nonlinear oscillators<br>Lasers, nonlinear optics<br>Nonequilibrium statistical mechanics<br>Nonlinear solid-state physics (semiconductors)<br>Josephson arrays<br>Heart cell synchronization<br>Neural networks<br>Immune system<br>Ecosystems<br>Economics</td>\r\n<td align=center><i>Spatio-temporal complexity</i><br>Nonlinear waves (shocks, solitons)<br>Plasmas<br>Earthquakes<br>General Relativity (Einstein)<br>Quantum field theory<br>Reaction-diffusion, biological and chemical waves<br>Fibrillation<br>Epilepsy<br>Turbulent fluids (Navier-Stokes)<br>Life\r\n</tr>\r\n</table>\r\n<p>\r\nThanks to Professor James Crutchfield and his <a href=\"http://cse.ucdavis.edu/~chaos/courses/nlp/\">PHY 250 Nonlinear Dynamics</a> class\r\n<p>\r\n<h2>References:</h2>\r\n<p>\r\nStrogatz, Steven H. <i>Nonlinear Dynamics and Chaos: With Applications to Physics, Biology</i>. Studies in Nonlinearity. Westview Press, 2001.\r\n<p>"}︡









