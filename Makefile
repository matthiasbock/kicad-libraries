
all: test.svg

%.svg: %.scad
	openscad $< -o temp.svg
	./postprocess temp.svg > $@
	rm temp.svg

clean:
	rm -fr *.svg
