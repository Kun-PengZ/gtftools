"""Doc.
GFF3, GTF
col 9s
col 1-8
col9

- class Fatheer # class 装载文件
- class Sun   # 解析文件细节
"""
import gzip
import gtftools


class Annotation:
    """Father class of GTF or GFF3.
    Loader of files.
    """
    REQUIRED_COLUMNS = [
        "seq_name", "source", "feature", "start",
        "end", "score", "strand", "frame",
        "attribute"
    ]

    def __init__(self, file):
        # 装载文件
        self.__file = file
        self._lines = None
        self.__load_file()

    def __load_file(self):
        self._lines = open(
            self.__file,
            'rt') if '.gz' not in self.__file else gzip.open(
            self.__file,
            'rt')


class Gff3(Annotation):
    """Gff3 class.
    Parse Gff3 files.
    """
    def to_gtf(self, file):
        # covert gff3 to gtf
        print('Covert Gff3 obj to Gtf obj...')
        f = open(file, 'wt') if '.gz' not in file else gzip.open(file, 'wt')

        counter_line = 0

        for line in self._lines:
            line = line.strip()
            counter_line += 1

            if line:
                if line.startswith('#'):
                    print(f'Skip #annotation line {counter_line}')
                    continue
                else:  # 核心计算
                    try:
                        seq_name, source, feature, start, end, \
                         score, strand, frame, attribute = line.split('\t')
                    except Exception as e:
                        raise gtftools.ParsingError(str(e))

                    attribute = {
                        k.rstrip(): v.strip()
                        for k, v in
                        [i.split('=') for i in attribute.split(';')]
                    }
                    print(attribute)
                    _dt = {
                        k: v
                        for k, v in zip(
                            self.REQUIRED_COLUMNS,
                            (seq_name, source, feature, start, end,
                             score, strand, frame, attribute)
                        )
                    }
                    # print(_dt)
                    # 逻辑判断，写个方法，处理_dt,保持代码整洁
                    final_dt = self.__to_gtf(dt=_dt)

                    if final_dt:
                        # 处理成功
                        pass
                    else:
                        # final_dt = None
                        continue
            else:
                continue
        f.close

    def __to_gtf(self, dt: dict) -> dict:
        pass


class Gtf(Annotation):
    """Gtf class.
        Parse Gtf files.
    """
    pass
