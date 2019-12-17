def calculate_fuel(mass)
    return mass / 3 - 2
end

def calculate_total_fuel_extra(file)
    total_fuel = 0
    File.open(file).each do |mass|
        fuel = calculate_fuel(mass.to_i)
        while fuel > 0
            total_fuel += fuel
            fuel = calculate_fuel(fuel)
        end
    end
    return total_fuel
end

total_fuel = calculate_total_fuel_extra('input.txt')
puts "La suma total de combustible es de: #{total_fuel}"
