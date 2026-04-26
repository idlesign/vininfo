from vininfo import Vin


def test_ford_au_year_at_position_11_not_10():
    """Synthetic 2004 Territory."""
    vin = Vin('6FPAAAJGAT4Z00001')

    assert vin.wmi == '6FP'
    assert vin.manufacturer == 'Ford Australia'
    assert vin.country == 'Australia'

    # Year is decoded from VIS index 1 (= VIN position 11), not the
    # SAE-default VIS index 0 (position 10).
    assert vin.years_code == '4'
    assert vin.years == [2004]

    # Position 9 ('A') is a model/body class code, not an SAE check digit,
    # so the global checksum check never matches for this brand.
    assert vin.verify_checksum() is False

    details = vin.details
    assert details.platform.code == 'J'
    assert details.platform.name == 'Australia'
    assert details.plant.code == 'G'
    assert details.plant.name == 'Broadmeadows (main line)'
    assert details.body_class.code == 'A'
    assert details.body_class.name == 'Territory'
    assert details.body_subclass.code == 'T'
    assert details.serial.code == '00001'


def test_ford_au_falcon_ute_year_letter_b_means_2011():
    """Synthetic 2011 Falcon Ute"""
    vin = Vin('6FPAAAJGCMBZ00002')
    assert vin.manufacturer == 'Ford Australia'
    assert vin.years_code == 'B'
    assert 2011 in vin.years
    assert vin.details.body_class.name == 'Commercial / Ute'
    assert vin.details.plant.name == 'Broadmeadows (main line)'


def test_ford_au_falcon_sedan_year_digit_2_means_2002():
    """Synthetic 2002 Falcon Sedan"""
    vin = Vin('6FPAAAJGSW2Z00003')
    assert vin.years_code == '2'
    assert vin.years == [2002]
    assert vin.details.body_class.name == 'Sedan / Wagon'


def test_ford_au_secondary_line_pre_2000():
    """Synthetic pre-2000 Falcon built on the Broadmeadows secondary line"""
    vin = Vin('6FPAAAJL0MSZ00004')
    assert vin.years_code == 'S'
    assert 1995 in vin.years
    assert vin.details.plant.name == 'Broadmeadows (secondary line)'
