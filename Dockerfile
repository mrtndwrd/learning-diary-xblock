FROM jbarciauskas/xblock-sdk
RUN mkdir -p /usr/local/src/learning-diary-xblock
VOLUME ["/usr/local/src/learning-diary-xblock"]
RUN echo "pip install -e /usr/local/src/learning-diary-xblock" >> /usr/local/src/xblock-sdk/install_and_run_xblock.sh
RUN echo "exec python /usr/local/src/xblock-sdk/manage.py \"\$@\"" >> /usr/local/src/xblock-sdk/install_and_run_xblock.sh
RUN chmod +x /usr/local/src/xblock-sdk/install_and_run_xblock.sh
ENTRYPOINT ["/bin/bash", "/usr/local/src/xblock-sdk/install_and_run_xblock.sh"]
CMD ["runserver", "0.0.0.0:8000"]
