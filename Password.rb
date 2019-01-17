def validate(thingToBeTested)
	thingToBeTested =~ /^(?=.*[a-zA-Z])(?=.*[0-9]).{8,}$/
end

puts "Enter your password"
if validate(gets.chomp)
    puts "Valid password"
else
    puts "Invalid password"
end

