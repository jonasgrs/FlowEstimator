# FlowEstimator
Static estimator for flow velocities in Domestic Heat Networks

The goal is to estimate, without the need for dynamic simulations, if the pipes in a DHC network might exceed the maximum allowed flow velocity.

In General, the flow velocity inside a pipe is determined by the following equations:

<img src="https://render.githubusercontent.com/render/math?math=v = \frac{\rho \cdot A}{\dot{m}}">

We can see, that the Flow velocity is a function of the Diameter and the Massflow inside the pipe.

The Massflow is determined by the Heatflow at the substations, the COP at the Substations and the Temperature Difference of the Network:

<img src="https://render.githubusercontent.com/render/math?math=\dot m_{nom} = \frac{\dot Q_{Network,max}}{c_{p,w} \cdot \Delta T_{Network}} = \frac{\dot Q_{Eva}}{c_{p,w} \cdot \Delta T_{Network}}  = \frac{\dot Q_{Heating} \cdot ( 1 - \frac{1}{COP} ) }{c_{p,w} \cdot \Delta T_{Network}}  \quad \left[ \frac{kg}{s} \right]">


The Diameter was laid out when the network was designed. Often, networks are designed with fixed assumptions for the specific pressure loss:


<img src="https://render.githubusercontent.com/render/math?math=D = \sqrt[5]{\frac{8 \lambda}{\rho} \cdot \frac{\dot m_{nom}^2}{\pi^2} \cdot \frac{1}{\frac{\Delta p_V}{\Delta L}}} = f \left( \dot m_{nom}, \frac{\Delta p_V}{\Delta L} \right)= f \left(\dot Q_{Heating}, COP, \Delta T_{Network}, \frac{\Delta p_V}{\Delta L} \right)">



