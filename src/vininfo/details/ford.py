from ._base import Detail, VinDetails


class FordAustraliaDetails(VinDetails):
    """Ford Australia VIN details extractor."""

    platform = Detail(('vds', 3), {
        'A': 'North America',
        'C': 'Europe / Britain',
        'J': 'Australia',
        'U': 'Japan (Mazda)',
    })

    plant = Detail(('vds', 4), {
        'G': 'Broadmeadows (main line)',
        'H': 'Brisbane',
        'K': 'Sydney',
        'L': 'Broadmeadows (secondary line)',
    })

    # Position 9 + 10 hold a 2-char body code, but the Detail descriptor
    # reads from a single section (vds ends at 9, vis starts at 10), so
    # split: body_class = pos 9, body_subclass = pos 10.
    body_class = Detail(('vds', 5), {
        'A': 'Territory',
        'C': 'Commercial / Ute',
        'S': 'Sedan / Wagon',
    })
    body_subclass = Detail(('vis', 0))

    # Brand binding in Vin.__init__ requires details.model.name to be truthy.
    model = body_class

    month = Detail(('vis', 2))

    serial = Detail(('vis', slice(3, None)))
