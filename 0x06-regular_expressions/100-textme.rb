#!/usr/bin/env ruby

def parse_message(input)
  regex = /(?<sender>\S+),(?<receiver>\S+),(?<flags>[A-Z]+)/
  match_data = input.match(regex)
  
  if match_data
    sender = match_data[:sender]
    receiver = match_data[:receiver]
    flags = match_data[:flags]
    
    puts "Sender: #{sender}"
    puts "Receiver: #{receiver}"
    puts "Flags: #{flags}"
  else
    puts "No match found in the input."
  end
end

# Accept one argument from the command line
if ARGV.length != 1
  puts "Usage: ruby script.rb <input>"
else
  parse_message(ARGV[0])
end
