def is_verb(label):
    """
    Checks if a given label is a verb accodring to STTS
    :param label:
    :return:
    """
    return label in ['VVFIN', 'VAFIN', 'VMFIN', 'VVINF', 'VAINF', 'VMINF', 'VVIMP', 'VVAIMP', 'VVPP', 'VAPP', 'VMPP', 'VVIZU']