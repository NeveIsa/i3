default:
	python3 -B tool_pub.py conf.d/local.yml

publish: default

config:
	python3 -B helper_conf.py conf.d/local.yml

clean:
	rm -rf __pycache__
	rm *.pyc

install:
	pip3 install -r req.txt
