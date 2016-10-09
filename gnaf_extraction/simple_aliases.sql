Copy -- Principle Addresses
(SELECT  
  address, 
  lot_number,
  number_first,
  number_last,
  street_name,
  street_type,
  street_suffix,
  locality_name,
  postcode,
  state
  --  '<lot_number>'||lot_number||'</lot_number> ' lot_number,
--  '<street_number_first>'||number_first||'</street_number_first> ' as street_number_first,
--  '<street_number_last'||number_last||'</street_number_last> ' as street_number_first,
--  '<street_name'||street_name||'</street_name> ' as street_name,
--  '<street_type'||street_type||'</street_type> ' as street_type,
--  '<street_suffix'||street_suffix||'</street_suffix> ' as street_suffix,
--  '<locality>'||locality_name||'</locality> ' as locality,
--  '<postcode>'||postcode||'</postcode> ' as postcode,
--  '<state_code>'||state||'</state_code> ' as state_code
 
  
FROM gnaf.address_principals
  tablesample system(0.01)
WHERE flat_number IS NULL
  AND level_number IS NULL)
To '/home/nokout/projects/au_address/gnaf_extraction/gnaf_data2.psv' With CSV DELIMITER '|';
--UNION
-- Alias Addresses
/*
SELECT *, 
  address, 
  locality_name as locality, 
  postcode, 
  state
FROM gnaf.address_aliases
  tablesample system(0.1)
WHERE flat_number IS NULL
  AND level_number IS NULL;
*/