# Puppet manifest to install and configure Nginx with a custom HTTP header

node default {
  # Ensure the Nginx package is installed
  package { 'nginx':
    ensure => installed,
  }

  # Ensure the Nginx service is running and enabled
  service { 'nginx':
    ensure    => running,
    enable    => true,
    require   => Package['nginx'],
  }

  # Define the custom Nginx configuration with the custom header
  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => template('nginx/default.erb'),
    require => Package['nginx'],
    notify  => Service['nginx'],
  }
}

# Define the custom template for the Nginx configuration
file { '/etc/puppetlabs/code/environments/production/modules/nginx/templates/default.erb':
  ensure  => file,
  content => @("EOF"),
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location / {
        try_files \$uri \$uri/ =404;
    }

    # Add custom header
    add_header X-Served-By <%= @hostname %>;
}
| EOF
}
