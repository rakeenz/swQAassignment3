from main import calc_category




def test_calc_category():
    assert calc_category(18.4) == "Underweight", "method doesnt work"
    assert calc_category(18.5) == "Normal Weight", "method doesnt work"
    assert calc_category(22.0) == "Normal Weight", "method doesnt work"
    assert calc_category(24.9) == "Normal Weight", "method doesnt work"
    assert calc_category(25.0) == "Overweight", "method doesnt work"
    assert calc_category(25.1) == "Overweight", "method doesnt work"
    assert calc_category(27.0) == "Overweight", "method doesnt work"
    assert calc_category(29.9) == "Overweight", "method doesnt work"
    assert calc_category(30.0) == "Obese", "method doesnt work"
