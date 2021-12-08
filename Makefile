SHELL           := /bin/bash
day             := day1
type            := sample
answer_template := answer_template.py
templates       := ${day}/sample.txt ${day}/input.txt ${day}/__init__.py ${day}/answer.py

.PHONY: run env

run: ${day}/${type}.txt ${day}/answer.py
	cat "${day}/${type}.txt" | python ${day}/answer.py

env: ${day} ${templates}

${day}:
	mkdir -p ${day}

${templates}:
	touch ${day}/sample.txt ${day}/input.txt ${day}/__init__.py; \
	cp -a ${answer_template} ${day}/answer.py
