# install flask
  exec { 'install python packages':
    command => 'pip3 install flask==2.1.0 flask_restful',
    path    => ['/usr/bin/'],
    unless  => '/usr/bin/test -f /usr/local/lib/python3.4/dist-packages/flask/app.py'
  }
