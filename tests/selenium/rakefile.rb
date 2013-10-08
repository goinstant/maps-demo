task :OSX106 do
	FileList['OSX-10.6/Chrome/sbs-maps.rb'].each { |file| ruby file }
end

task :OSX108 do
	FileList['OSX-10.8/Chrome/sbs-maps.rb'].each { |file| ruby file }
end

task :WIN7 do
	FileList['Win-7/Chrome/sbs-maps.rb'].each { |file| ruby file }
end

task :WIN8 do
	FileList['Win-8/Chrome/sbs-maps.rb'].each { |file| ruby file }
end

task :WINXP do
	FileList['Win-XP/Chrome/sbs-maps.rb'].each { |file| ruby file }
end

multitask :default => [:WINXP, :WIN7, :WIN8, :OSX108, :OSX106] do
	puts "Chrome tests successfully completed!"
	puts "+      o     +              o   "
	puts "    +             o     +       +"
	puts "o          +"
	puts "    o  +           +        +"
	puts "+        o     o       +        o"
	puts "-_-_-_-_-_-_-_,------,      o "
	puts "_-_-_-_-_-_-_-|   /\_/\  "
	puts "-_-_-_-_-_-_-~|__( ^ .^)  +     +  "
	puts "_-_-_-_-_-_-_-""  ""      "
	puts "+      o         o   +       o"
	puts "    +         +"
	puts "o        o         o      o     +"
	puts "    o           +"
	puts "+      +     o        o      +    "
end

task :OSX106s do
	FileList['OSX-10.6/Safari/sbs-maps.rb'].each { |file| ruby file }
end

task :OSX108s do
	FileList['OSX-10.8/Safari/sbs-maps.rb'].each { |file| ruby file }
end

multitask :default => [:OSX108s, :OSX106s] do
	puts "Safari tests successfully completed!"
	puts "+      o     +              o   "
	puts "    +             o     +       +"
	puts "o          +"
	puts "    o  +           +        +"
	puts "+        o     o       +        o"
	puts "-_-_-_-_-_-_-_,------,      o "
	puts "_-_-_-_-_-_-_-|   /\_/\  "
	puts "-_-_-_-_-_-_-~|__( ^ .^)  +     +  "
	puts "_-_-_-_-_-_-_-""  ""      "
	puts "+      o         o   +       o"
	puts "    +         +"
	puts "o        o         o      o     +"
	puts "    o           +"
	puts "+      +     o        o      +    "
end

task :WIN7f do
	FileList['Win-7/Firefox/sbs-maps.rb'].each { |file| ruby file }
end

task :WIN8f do
	FileList['Win-8/Firefox/sbs-maps.rb'].each { |file| ruby file }
end

task :WINXPf do
	FileList['Win-XP/Firefox/sbs-maps.rb'].each { |file| ruby file }
end

multitask :default => [:WINXPf, :WIN7f, :WIN8f] do
	puts "Firefox tests successfully completed!"
	puts "+      o     +              o   "
	puts "    +             o     +       +"
	puts "o          +"
	puts "    o  +           +        +"
	puts "+        o     o       +        o"
	puts "-_-_-_-_-_-_-_,------,      o "
	puts "_-_-_-_-_-_-_-|   /\_/\  "
	puts "-_-_-_-_-_-_-~|__( ^ .^)  +     +  "
	puts "_-_-_-_-_-_-_-""  ""      "
	puts "+      o         o   +       o"
	puts "    +         +"
	puts "o        o         o      o     +"
	puts "    o           +"
	puts "+      +     o        o      +    "
end

task :WIN7i do
	FileList['Win-7/IE9/sbs-maps.rb'].each { |file| ruby file }
end

task :WIN8i do
	FileList['Win-8/IE10/sbs-maps.rb'].each { |file| ruby file }
end

task :WINXPi do
	FileList['Win-XP/IE8/sbs-maps.rb'].each { |file| ruby file }
end

multitask :default => [:WINXPi, :WIN7i, :WIN8i] do
	puts "IE tests successfully completed!"
	puts "+      o     +              o   "
	puts "    +             o     +       +"
	puts "o          +"
	puts "    o  +           +        +"
	puts "+        o     o       +        o"
	puts "-_-_-_-_-_-_-_,------,      o "
	puts "_-_-_-_-_-_-_-|   /\_/\  "
	puts "-_-_-_-_-_-_-~|__( ^ .^)  +     +  "
	puts "_-_-_-_-_-_-_-""  ""      "
	puts "+      o         o   +       o"
	puts "    +         +"
	puts "o        o         o      o     +"
	puts "    o           +"
	puts "+      +     o        o      +    "
end
