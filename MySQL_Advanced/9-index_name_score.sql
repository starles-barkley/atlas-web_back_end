-- Create an index on the first letter of the name
CREATE INDEX idx_name_first ON names (SUBSTRING(name, 1, 1));
