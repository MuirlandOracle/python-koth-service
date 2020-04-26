pip3 install -r requirements.txt
cp koth.py /usr/bin
cp koth.service /etc/systemd/system
systemctl start koth
systemctl enable koth
