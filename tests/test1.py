import gtftools
from gtftools import Gff3


def test_info():
    # 测试基本信息
    print(gtftools.__version__)
    print(gtftools.__author__)
    print(gtftools.__email__)


def test_gff3():
    gff3 = Gff3(file='data/test.gff3')
    gff3.to_gtf('tests/test_to_gtf.gtf')


def main():
    # 单元测试
    test_info()
    test_gff3()
    pass


if __name__ == "__main__":
    main()
