default: docs


.PHONY: docs
docs:
	mkdir -p doxygen/xml
	doxygen
	sphinx-build . docs/


.PHONY: build
build:
	mkdir -p build
	gcc -o build/test src/test.c


.PHONY: clean
clean:
	rm -rf doxygen
	rm -rf docs
	rm -rf _images
	rm -rf build
