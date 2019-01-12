def set_power_contract(power, contract, unit_price=None, init_fee=None, read_power_date=None):
    """
    设置电表和合同的关系
    :param power:
    :return:
    """
    if PowerContract.objects.filter(power_meter=power, contract=contract).exists() or not contract:
        return True

    # 先合同后绑表
    # 判断合同是否是预付费/抄表
    charge = u'prepayment'
    power_unit_price = unit_price
    if not unit_price:
        is_meter = False
        for util in contract.utilities.all():
            if util.name == 'power_fees' and util.charge == 'prepayment':  # util.charge == 'by_meter' or
                charge = util.charge
                power_unit_price = util.unit_price
                is_meter = True
                # if not init_fee:  # 先入合同后绑表获取充值金额 都不显示
                #     init_fee = util.month_price
                break
        if not is_meter:
            return True

    public_power = SmartPowerMeter.objects.filter(bind=1, style=1, serial_id=power.master).last()
    if not public_power:
        logger.warning(msg=u'创建电表合同初始关系出错')
        return False

    if power_unit_price:
        power.price = power_unit_price
        power.save()

    # 没指定读表时间 去表最后一次读数
    args = dict(power_meter=power)
    node_record = SmartPowerRecord.objects.filter(**args).last()
    if read_power_date:
        args['read_date'] = format_str2date(read_power_date)
        node_record = SmartPowerRecord.objects.filter(**args).last()
    node_value = node_record.num if node_record else 0

    data = dict(contract=contract, power_meter=power,
                init_num=node_value, int_num_date=format_datetime(datetime.now()),
                charge=charge)

    tmp = dict()
    if init_fee:
        tmp['init_money'] = init_fee
        tmp['prepayment_money'] = init_fee

    # 换表初始金额取上一次的值，用在合同详情里显示使用  解绑余额清零
    # 剩余金额＝上次表的剩余金额＋这次新增的初始纪录
    # 换表  合同依旧存在
    # pre_pc = PowerContract.objects.filter(contract=contract).last()
    # if pre_pc:
    #     tmp['is_prepower'] = 1
    #     tmp['init_money'] = pre_pc.init_num if pre_pc else 0
    #     tmp['pre_prepower_money'] = pre_pc.prepayment_money if pre_pc else 0
    #     tmp['prepayment_money'] = (pre_pc.prepayment_money if pre_pc else 0) + init_fee

    data.update(**tmp)
    pc = PowerContract(**data)
    pc.save()
    return True