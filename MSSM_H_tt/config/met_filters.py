# coding: utf-8

"""
Definition of MET filter flags.
"""

import order as od

from columnflow.util import DotDict


def add_met_filters(config: od.Config) -> None:
    """
    Adds all MET filters to a *config*.

    Resources:
    https://twiki.cern.ch/twiki/bin/viewauth/CMS/MissingETOptionalFiltersRun2
    """
    year = config.campaign.x.year

    if year == 2016:
        filters = [
            "Flag.goodVertices",
            "Flag.globalSuperTightHalo2016Filter",
            "Flag.HBHENoiseFilter",
            "Flag.HBHENoiseIsoFilter",
            "Flag.EcalDeadCellTriggerPrimitiveFilter",
            "Flag.BadPFMuonFilter",
            "Flag.BadPFMuonDzFilter",
            "Flag.eeBadScFilter",
        ]
    elif year in (2022, 2023, 2024):
        filters = [
            "Flag.goodVertices",
            "Flag.globalSuperTightHalo2016Filter",
            "Flag.EcalDeadCellTriggerPrimitiveFilter",
            "Flag.BadPFMuonFilter",
            "Flag.BadPFMuonDzFilter",
            "Flag.hfNoisyHitsFilter",
            "Flag.eeBadScFilter",
        ]

        # Required for 2024, but not for 2022 and 2023.
        if year not in (2022, 2023):
            filters.append("Flag.ecalBadCalibFilter")
    
    else:
        filters = [
            "Flag.goodVertices",
            "Flag.globalSuperTightHalo2016Filter",
            "Flag.HBHENoiseFilter",
            "Flag.HBHENoiseIsoFilter",
            "Flag.EcalDeadCellTriggerPrimitiveFilter",
            "Flag.BadPFMuonFilter",
            "Flag.BadPFMuonDzFilter",
            "Flag.hfNoisyHitsFilter",
            "Flag.eeBadScFilter",
        ]
    
    # same filter for mc and data, but still separate
    filters = {
        "mc": filters.copy(),
        "data": filters.copy(),
    }

    config.x.met_filters = DotDict.wrap(filters)
