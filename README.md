Outputs to robot: 

set heading 
velocity in fwd direction 


Input to Code: 

odom of turtlbots from vicon 
orientation from internal odometry from bot


v = vel bot in x direction 
theta = heading of bot 

dx = v*cos(theta)
dy = v*sin(theta)

dtheta = w -> w = u(t) : controller input 

dynamics of robot fully defined by: 
 dr = v*exp(j*theta), dtheta = u(t)

 -> normalise speed to 1

 blabla 

u(t)i = -k/n sum(sin(thetaj - thetai))