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
<<<<<<< HEAD
=======
    DROP_ATTRIBUTES = (
        # chrom
        'chromosome', 'scaffold',
        # gene
        'gene', 'pseudogene', 'ncRNA_gene', 'V_gene_segment',
        'D_gene_segment', 'J_gene_segment', 'C_gene_segment',
        # exon
        'exon',
        #
        'biological_region',
        'pseudogenic_transcript', 'unclassified_transcript',
    )

>>>>>>> 3b3960a (Initialize gtftools repository)
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
<<<<<<< HEAD
                    print(attribute)
=======
                    # print(attribute)
>>>>>>> 3b3960a (Initialize gtftools repository)
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
<<<<<<< HEAD
                        pass
=======
                        # print(final_dt)
                        line = ''

                        for k, v in final_dt.items():
                            if k != self.REQUIRED_COLUMNS[8]:
                                line += f'{v}\t'
                            else:
                                attri = ''

                                for k2, v2 in v.items():
                                    attri += f'{k2} "{v2}"; '
                                attri = attri.rstrip()
                                line += attri + '\n'
                        f.write(line)
>>>>>>> 3b3960a (Initialize gtftools repository)
                    else:
                        # final_dt = None
                        continue
            else:
                continue
<<<<<<< HEAD
        f.close

    def __to_gtf(self, dt: dict) -> dict:
        pass
=======
        f.close()

    def __to_gtf(self, dt: dict) -> dict:
        feature = dt[self.REQUIRED_COLUMNS[2]]
        if feature in self.DROP_ATTRIBUTES:
            return
        else:
            attribute = dt[self.REQUIRED_COLUMNS[8]]

            # print('-' * 10)
            # print('DEBUG', feature, attribute)

            _id = attribute.get('ID', None)
            parent = attribute.get('Parent', None)

            gene_id = ''
            transcript_id = ''

            if feature in ['five_prime_UTR', 'three_prime_UTR', 'CDS']:
                _dt = {'five_prime_UTR': 'five_prime_utr', 'three_prime_UTR': 'three_prime_utr', 'CDS': 'CDS'}
                feature = _dt[feature]
                transcript_id = parent.split(':')[1] if 'transcript' in parent else ''
            elif 'RNA' in feature:
                transcript_id = _id.split(':')[1] if 'transcript' in _id else ''
                gene_id = parent.split(':')[1] if 'gene' in parent else ''

            # print(f'DEBUG: {feature}, {gene_id}, {transcript_id}')
            dt_info = {
                'gene_id': gene_id,
                'transcript_id': transcript_id,
            }

            for k, v in attribute.items():
                if k[0].islower():
                    dt_info[k] = v

            dt[self.REQUIRED_COLUMNS[2]] = feature
            dt[self.REQUIRED_COLUMNS[8]] = dt_info
            return dt
>>>>>>> 3b3960a (Initialize gtftools repository)


class Gtf(Annotation):
    """Gtf class.
        Parse Gtf files.
    """
    pass
