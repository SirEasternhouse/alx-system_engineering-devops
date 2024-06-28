# installation of flask package


python::pip { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
