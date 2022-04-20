#create a manifest that kills a process named killmenow
exec { 'pkill -x killmenow':
  path  => '/usr/bin:/usr/sbin:/bin'
}