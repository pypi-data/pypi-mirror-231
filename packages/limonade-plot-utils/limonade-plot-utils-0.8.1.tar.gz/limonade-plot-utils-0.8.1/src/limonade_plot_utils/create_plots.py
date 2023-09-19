from limonade.data import load_config
from limonade.utils import get_limonade_config
from pathlib import Path
import json

def create_plots():
    """
        Create_plots reads a detector configuration and creates simple plots for each channel.

        :return:
        """

    # setup path config with global configuration directory
    path_cfg = get_limonade_config()
    det = parse_args()

    # Do the thang
    for ch_idx, ch in enumerate(det.cfg.det['ch_cfg']):
        plot_cfg = {"name": det.cfg.det['name'] + '_' + ch['name'],
                    "plot_cfg": [
                                 {"plot_name": "Energy",
                                  "axes": [{"channel": ch_idx, "data": "energy", "bin_width": 1, "range": [0, 3000]}],
                                            "gates": []}
                    ],
                    "xscale": "linear",
                    "yscale": "log",
                    "zscale": "log",
                    "nolegend": True
                    }
        print(path_cfg)
        plot_dir = Path(path_cfg['cfg_dir']) / 'plotcfg'
        if not plot_dir.exists():
            print('Creating plot configuration directory.')
            plot_dir.mkdir()
        with (plot_dir / (plot_cfg['name'] + '_plotcfg.json')).open('w') as fil:
            json.dump(plot_cfg, fil)


def parse_args():
    import argparse
    parser = argparse.ArgumentParser(description='Create basic plot configurations for a detector.')
    parser.add_argument('detector', metavar='det_cfg', type=str,
                        help='Name of the detector configuration.')
    args = parser.parse_args()
    print(args.detector)

    # here we read the global configuration of the detector, so the local path is irrelevant.
    confd = load_config(None, det_name=args.detector, from_global_conf=True)
    args.cfg = confd
    return args

