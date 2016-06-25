CXXFLAGS= -g -Wall -Wextra -Wfloat-equal -Wswitch-default -Wswitch-enum -Wshadow -Wwrite-strings -Wpointer-arith -Wcast-qual -Wredundant-decls -Winit-self -Wno-switch-enum -Wno-unused-but-set-parameter -Wno-unused-parameter


all: Smartcity


Smartcity: main.o
	g++ $^ -o SmartCity -lopencv_core -lopencv_imgproc -lopencv_highgui -lopencv_objdetect
	
main.o : 



clean:
	rm -f ./*.o SmartCity