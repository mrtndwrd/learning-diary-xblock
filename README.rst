README for Learning Diary XBlock

Testing with Docker
-------------------

This XBlock comes with a Docker test environment ready to build, based on the xblock-sdk workbench. To build it, run::

        $ docker build -t learningdiary .

Then, to run the docker image you built::

        $ docker run -d -p 8000:8000 --name learningdiary learningdiary

The XBlock SDK Workbench, including this XBlock, will be available on the list of XBlocks at http://localhost:8000
