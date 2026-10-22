import json
logos=[("progressive","Progressive"),("travelers-2","Travelers"),("hartford","The Hartford"),("zurich-logo-big","Zurich"),("plymouth-rock-logo","Plymouth Rock"),("farmers","Farmers"),("foremost","Foremost"),("franklin-mutual-insurance","Franklin Mutual"),("stillwater-logo-stacked","Stillwater"),("next-insurance-logo","NEXT Insurance"),("Coterie_Logo-scaled","Coterie"),("amtrust-financial-logo-vector","AmTrust Financial"),("wright-flood-logo-5","Wright Flood"),("192-1925658_lancerlogo-lancer-insurance-hd-png-download","Lancer Insurance"),("phila_logo","Philadelphia Insurance"),("providence-logo","Providence"),("skylands","Skylands"),("logo_nationalgeneral","National General"),("AmericanNational","American National"),("AEIG-Logo-300px2","American European"),("amig_logo","American Modern")]
li=''.join(f'<li><img src="logos/{f}.webp" alt="{n}" loading="lazy" decoding="async"></li>' for f,n in logos)
mq=f'<ul class="mtrack">{li}</ul><ul class="mtrack" aria-hidden="true">{li}</ul>'
cov={"auto":("Auto","🚗","Daily drivers, collectible autos and the family fleet.",["Auto","Collectible Autos","Motorcycle","Moped","Motorhome","Camper"]),
"home":("Home","🏠","Homeowners, condo and mobile home coverage.",["Homeowners","Condo","Mobile Home","Flood","Umbrellas"]),
"renters":("Renters","🔑","Protect your belongings and your rental properties.",["Renters","Renter properties up to 4 family","Umbrellas"]),
"life":("Life","❤️","Coverage that looks after the people you love.",["Life"]),
"business":("Business","🏪","Commercial coverage for local shops, trades and landlords.",["General Liability","Property Coverage","Workers Compensation","Excess Liability","Commercial Flood","Builders Risks","Delivery Vehicles","Trucks/Towing"]),
"rec":("Boat & Rec","⛵","Weekend toys, on land and water.",["Motorboat (Inboard)","Motorboat (Outboard)","Motorboat (Stern Drive)","Sail Boat","Jet Ski / Wave Runner","ATV’s & Off Road Vehicles","Snowmobile"])}
tabs=''.join(f'<button role="tab" data-k="{k}" aria-selected="{"true" if i==0 else "false"}"><span class="ic">{v[1]}</span>{v[0]}</button>' for i,(k,v) in enumerate(cov.items()))
P=["Auto","Collectible Autos","Motorcycle","ATV’s","Off Road Vehicles","Snowmobile","Jet Ski","Wave Runner","Motorboat (Inboard)","Motorboat (Outboard)","Motorboat (Stern Drive)","Life","Mobile Home","Homeowners","Flood","Renter properties up to 4 family","Umbrellas","Motorhome","Condo","Camper","Sail Boat","Moped"]
B=["Beauty Salons","Auto Repair Shops","General Liability","Apartment Buildings","Restaurants/Pizzerias","Property Coverage","Bars/Taverns","Bakeries","Offices","Builders Risks","Contractors","Trucks/Towing","Excess Liability","Delivery Vehicles","Workers Compensation","Grocery Stores","Retail","Commercial Flood"]
ch=lambda L:''.join(f'<li>{x}</li>' for x in L)
h=open('tpl.html').read().replace('%MQ%',mq).replace('%TABS%',tabs).replace('%COV%',json.dumps(cov,ensure_ascii=False)).replace('%PERS%',ch(P)).replace('%BUS%',ch(B))
open('index.html','w').write(h)
