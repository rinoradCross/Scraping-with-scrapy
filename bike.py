import scrapy


class BikeSpider(scrapy.Spider):
    name = 'bike'
    allowed_domains = ['carandbike.com']
    start_urls = ['https://www.carandbike.com/new-bikes/models']

    def parse(self, response):
        bikes = response.xpath("//ul[@class='newmodel-bike__grid grid grid__gap15 h__mb30']/li")
        for bike in bikes:
            url = bike.xpath(".//div/a/@href").get()

            yield scrapy.Request(url = url,callback = self.parse_bike)
        next_page = response.xpath("//li[@class='pagination__item next']/a/@href").get()
        if next_page:
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_url, callback=self.parse) 

    def parse_bike(self,response):
        name = response.xpath("//h1[@class='title']/text()").get()
        price = response.xpath("//span[@class='js-onroad-price']/text()").get()
        mileage = response.xpath("//ul[@class='row row-g_5']/li[3]/div/div[2]/text()").get()
        mileage = mileage.strip()
        divisions = response.xpath("//div[@class='row row-g_20']/div")
        for division in divisions:
            specifications = division.xpath(".//div")
            for spec in specifications:
                section = spec.xpath(".//h3/text()").get()
                if section == "Transmission":
                    spec_title = spec.xpath(".//ul/li[1]/div/span[1]/text()").get()
                    num_gears = "N/A"
                    if spec_title == "No. Of Gears":
                        num_gears = spec.xpath(".//ul/li[1]/div/span[2]/text()").get()
                elif section == "Electricals":
                    spec_title = spec.xpath(".//ul/li[1]/div/span[1]/text()").get()
                    battery = "N/A"
                    if spec_title == "Battery":
                        battery = spec.xpath(".//ul/li[1]/div/span[2]/text()").get()
                elif section == "Engine":
                    spec_title = spec.xpath(".//ul/li[1]/div/span[1]/text()").get()
                    engine_cc = "N/A"
                    if spec_title == "Engine CC":
                        engine_cc = spec.xpath(".//ul/li[1]/div/span[2]/text()").get()
                    spec_title = spec.xpath(".//ul/li[2]/div/span[1]/text()").get()
                    num_cylinder = "N/A"
                    if spec_title == "No Of Cylinder":
                        num_cylinder = spec.xpath(".//ul/li[2]/div/span[2]/text()").get()
                        num_cylinder = num_cylinder.strip()
                    spec_title = spec.xpath(".//ul/li[3]/div/span[1]/text()").get()
                    max_power = "N/A"
                    if spec_title == "Max Power":
                        max_power = spec.xpath(".//ul/li[3]/div/span[2]/text()").get()
                    spec_title = spec.xpath(".//ul/li[4]/div/span[1]/text()").get()
                    max_torque = "N/A"
                    if spec_title == "Max Torque":
                        max_torque = spec.xpath(".//ul/li[4]/div/span[2]/text()").get()
                    spec_title = spec.xpath(".//ul/li[5]/div/span[1]/text()").get()
                    valves = "N/A"
                    if spec_title == "Valves Per Cylinder":
                        valves = spec.xpath(".//ul/li[5]/div/span[2]/text()").get()
                        valves = valves.strip()
                    spec_title = spec.xpath(".//ul/li[6]/div/span[1]/text()").get()
                    fuel_delivery = "N/A"
                    if spec_title == "Fuel Delivery":
                        fuel_delivery = spec.xpath(".//ul/li[6]/div/span[2]/text()").get()
                    
                    spec_title = spec.xpath(".//ul/li[8]/div/span[1]/text()").get()
                    starting_mech = "N/A"
                    if spec_title == "Starting Mechanism":
                        starting_mech = spec.xpath(".//ul/li[8]/div/span[2]/text()").get()
                elif section == "Dimension and Weight":
                    spec_title = spec.xpath(".//ul/li[1]/div/span[1]/text()").get()
                    kerb_weight = "N/A"
                    if spec_title == "Kerb Weight":
                        kerb_weight = spec.xpath(".//ul/li[1]/div/span[2]/text()").get()
                    spec_title = spec.xpath(".//ul/li[2]/div/span[1]/text()").get()
                    length = "N/A"
                    if spec_title == "Length":   
                        length = spec.xpath(".//ul/li[2]/div/span[2]/text()").get()
                    spec_title = spec.xpath(".//ul/li[3]/div/span[1]/text()").get()
                    width = "N/A"
                    if spec_title == "Width":    
                        width = spec.xpath(".//ul/li[3]/div/span[2]/text()").get()
                    spec_title = spec.xpath(".//ul/li[4]/div/span[1]/text()").get()
                    height = "N/A"
                    if spec_title == "Height":    
                        height = spec.xpath(".//ul/li[4]/div/span[2]/text()").get()
                    spec_title = spec.xpath(".//ul/li[5]/div/span[1]/text()").get()
                    wheel_base = "N/A"
                    if spec_title == "Wheelbase":    
                        wheel_base = spec.xpath(".//ul/li[5]/div/span[2]/text()").get()
                    spec_title = spec.xpath(".//ul/li[6]/div/span[1]/text()").get()
                    ground_clearance = "N/A"
                    if spec_title == "Ground Clearance":    
                        ground_clearance = spec.xpath(".//ul/li[6]/div/span[2]/text()").get()
                    spec_title = spec.xpath(".//ul/li[7]/div/span[1]/text()").get()
                    seat_height = "N/A"
                    if spec_title == "Seat Height":    
                        seat_height = spec.xpath(".//ul/li[7]/div/span[2]/text()").get()
                elif section == "Wheel and Tyres":
                    spec_title = spec.xpath(".//ul/li[1]/div/span[1]/text()").get()
                    wheel_size = "N/A"
                    if spec_title == "Wheel Size":    
                        wheel_size = spec.xpath(".//ul/li[1]/div/span[2]/text()").get()
        yield{
            'name' : name,
            'price' : price,
            'mileage' : mileage,
            'kerb_weight' : kerb_weight,
            'length' : length,
            'width' : width,
            'height' : height,
            'wheel_base' : wheel_base,
            'ground_clearance' : ground_clearance,
            'seat_height' : seat_height,
            'engine_cc' : engine_cc,
            'num_cylinder' : num_cylinder,
            'max_power' : max_power,
            'max_torque' : max_torque,
            'valves' : valves,
            'fuel_delivery' : fuel_delivery,
            'starting_mech' : starting_mech,
            'num_gears' : num_gears,
            'wheel_size' : wheel_size,
            'battery' : battery
        }
        
        
        
