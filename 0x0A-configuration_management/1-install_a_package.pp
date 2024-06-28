class { 'python':
  provider => 'system',
}

python::pip { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
