#!/usr/bin/env ruby

# Check if the argument contains the word "School"
def match_school(argument)
  regex = /School/
     if argument =~ regex
       puts "The argument '#{argument}' contains the word 'School'."
     else
       puts "The argument '#{argument}' does not contain the word 'School'."
     end
end
# Accept one argument from the command line
if ARGV.length != 1
  puts "Usage: ruby script.rb <argument>"
else
  match_school(ARGV[0])
end
