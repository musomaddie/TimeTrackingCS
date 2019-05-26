float[] xspeed = new float[5];
float [] x = new float[5]
for (int i = 0; i < 5; i++ ) {
	xspeed[i] = random(1.15, 1.2);
	x[i] = // wherever you want the ball to start! 
}

// same for x and y. Should have 4 different arrays each of size 5.
// same for y speed etc.


// When you get to adding speed:
for (int i = 0; i < 5; i++) {
	x[i] += xspeed[i];
	y[i] += yspeed[i];
}


// performing all the checks 
// 1) loop through every ball
for (int i = 0; i < 5; i++) {
	// perform each check. 
	// Check if THIS BALL hits the bottom
	if (y[i] > height) {
		yspeed[i] = yspeed[i] * -0.95;
	}
	
	// the rest of the checks 
}
