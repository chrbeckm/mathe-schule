ifeq (,$(shell sh -c 'cygpath --version 2> /dev/null'))
  # Unix
  pwd := $$(pwd)
  translate = $1
else
  # Windows mit MSys2/Cygwin
  pwd := $$(cygpath -m "$$(pwd)")
  translate = $(shell echo '$1' | sed 's/:/;/g')
endif

all: build/5.pdf build/5l.pdf

build/koordleer.pdf: koord.py ../matplotlibrc ../header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python koord.py
build/koordpunkte.pdf: build/koordleer.pdf
build/koordgeraden.pdf: build/koordleer.pdf

build/5.pdf:build/koordleer.pdf

build/5.pdf: FORCE | build
	  TEXINPUTS="$(call translate,build:)" \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	5.tex

build/5l.pdf: build/koordpunkte.pdf \
		build/koordgeraden.pdf

build/5l.pdf: FORCE | build
	  TEXINPUTS="$(call translate,build:)" \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	5l.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
