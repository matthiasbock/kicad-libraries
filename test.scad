
// by default all measures in millimeters
include <imperial.scad>;

// rendering parameters
$fn=100;

module pad()
{
    square([10,10]);
}

module pads()
{
    for (i = 1; i ...
    pad();
}

pads();
