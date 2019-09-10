default:
	python3 -B tool_pub.py conf.d/local.yml
	rm -rf __pycache__

publish: default

config:
	python3 -B helper_conf.py conf.d/local.yml

clean:
	rm -rf __pycache__

install:
	pip3 install -r req.txt
