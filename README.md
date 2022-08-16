# LQG-control-of-gantry-cranes
_____
## Features
1. Get a state-space representation of a gantry crane linear system
2. Obtain matrices A, B, C, D, U for a time-domain simulation of system
x' = A*x + B*U 
y = C*x + D*U
3. Model disturbances for inputs and noise for sensors as gaussian processes
4. Build Kalman Filter for the linear system
5. Plotting time domain response gor the system
6. Model LQR control
____
## Getting Started
Use the package manager pip or conda to install slycot and control.
More information on https://github.com/python-control/python-control/tree/0.9.1#installation

You also need Numpy and Matplotlib.pyplot
___
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.
___
## License
See https://github.com/justsuvorov/LQG-control-of-gantry-cranes/blob/main/LICENSE.md
