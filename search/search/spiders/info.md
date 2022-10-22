## THOMANN
total_pages = response.css('button[appearance = secondary]::text').getall() # Pagination 
product_page = response.css('div.product a.product__content::attr(href)') 
title = response.css('h1::text').get()
price = response.css('div.price').get()
image = response.css('picture.ZoomImagePicture img::attr(src)').get()
desc1 = response.css('h2::text').get()
desc2 = response.css('ul.fx-list.product-text__list li span::text').getall()
description = desc2 + desc1 + title

## SWEETWATER
product_page = response.css('h2.product-card__name a::attr(href)').getall()
next_page = response.urljoin(response.css('li.next a::attr(href)').get()) # Pagination
title = response.css('h1.product__name span::text').getall()
price = response.css('div.product-price--final price dollars::text').get()
image = response.css('div img::attr(src)').get()
description = response.css('div.webtext-block.webtext-block--mixed-content p').get()