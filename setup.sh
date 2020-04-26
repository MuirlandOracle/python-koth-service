pip3 install -r requirements.txt
touch /root/king.txt
mv koth.py /usr/bin
mv koth.service /etc/systemd/system
systemctl start koth
systemctl enable koth
