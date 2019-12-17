def calculate_fuel(mass)
    return (mass/3).round-2
end

def calculate_total_fuel(file)
    total_fuel = 0
    File.open(file).each do |mass|
        fuel = calculate_fuel(mass.to_i)
        total_fuel += fuel
    end
    return total_fuel
end

total_fuel = calculate_total_fuel('input.txt')
puts "La suma total de combustible es de: #{total_fuel}"