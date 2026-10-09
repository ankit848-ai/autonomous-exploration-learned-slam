# -*- coding: utf-8 -*-
r"""
Upgrades D:\ROBOTICS PROJECT 7TH SEM\README.md

  1. Badge strip + tagline under the H1 title
  2. "Repository" section listing BOTH GitHub accounts
  3. Citation (BibTeX) + License section at the end

Purely additive - it deletes none of the existing prose, and it is safe to
run twice (each block is guarded by an HTML marker comment).

Run with:
    python "D:\ROBOTICS PROJECT 7TH SEM\06_Build_Scripts\readme_upgrade.py"
"""
import io

README = r"D:\ROBOTICS PROJECT 7TH SEM\README.md"

PRIMARY = "https://github.com/Ankit-builds1/autonomous-exploration-learned-slam"
MIRROR = "https://github.com/ankit848-ai/autonomous-exploration-learned-slam"

HEADER = """
<p align="center">
  <img src="https://img.shields.io/badge/ROS2-Humble-22314E?style=flat-square&logo=ros&logoColor=white" alt="ROS2 Humble">
  <img src="https://img.shields.io/badge/Gazebo-Classic%2011-FF6C00?style=flat-square" alt="Gazebo Classic 11">
  <img src="https://img.shields.io/badge/Nav2-navigation__launch-5A2D82?style=flat-square" alt="Nav2">
  <img src="https://img.shields.io/badge/SLAM%20Toolbox-online__async-2E8B57?style=flat-square" alt="SLAM Toolbox">
  <img src="https://img.shields.io/badge/PPO-Stable--Baselines3%202.9-EE4C2C?style=flat-square&logo=pytorch&logoColor=white" alt="PPO">
  <img src="https://img.shields.io/badge/Python-3.10-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python 3.10">
  <img src="https://img.shields.io/badge/license-MIT-black?style=flat-square" alt="MIT">
</p>

<p align="center">
  <b>A learned exploration policy, trained entirely in an abstract simulator,
  that transfers to the real ROS2 navigation stack and beats the hand-tuned
  heuristic it was benchmarked against.</b><br>
  <sub>Reinforcement learning &middot; frontier-based exploration &middot; online SLAM
  &middot; natural-language mission control</sub>
</p>

<!--UPGRADE-HEADER-->
"""

REPOS = """
---

## Repository

This project is published on both of the author's GitHub accounts. The two
repositories hold identical content; either one can be cloned.

| | Account | URL |
|---|---|---|
| **Primary** | `Ankit-builds1` | {primary} |
| **Mirror** | `ankit848-ai` | {mirror} |

```bash
git clone {primary}.git
cd autonomous-exploration-learned-slam
```

The ROS2 package itself lives in [`01_Source_Code/explore_nav/`](01_Source_Code/explore_nav);
everything else in the tree is evidence - trained weights, TensorBoard logs,
saved maps, figures and the written report.

<!--UPGRADE-REPOS-->
""".format(primary=PRIMARY, mirror=MIRROR)

CITE = """
---

## Citing this work

```bibtex
@misc{{dash2026autonomousexploration,
  author       = {{Ankit Dash}},
  title        = {{Autonomous Exploration with Learned SLAM: A Reinforcement-Learned
                  Frontier Selection Policy Evaluated Against a Hand-Tuned Heuristic}},
  year         = {{2026}},
  howpublished = {{\\url{{{primary}}}}},
  note         = {{Final-year BTech CSE (DAML) project,
                  Centurion University of Technology and Management}}
}}
```

## Acknowledgements

Built on [ROS2 Humble](https://docs.ros.org/en/humble/),
[Nav2](https://navigation.ros.org/),
[SLAM Toolbox](https://github.com/SteveMacenski/slam_toolbox),
[TurtleBot3](https://emanual.robotis.com/docs/en/platform/turtlebot3/overview/),
[Gazebo Classic](https://classic.gazebosim.org/),
[Gymnasium](https://gymnasium.farama.org/) and
[Stable-Baselines3](https://stable-baselines3.readthedocs.io/).
The frontier-detection formulation follows Yamauchi (1997).

## License

Released under the MIT License - see [`LICENSE`](LICENSE).
Upstream ROS2, Nav2, SLAM Toolbox, TurtleBot3 and Gazebo components remain
under their own licences.

<!--UPGRADE-CITE-->
""".format(primary=PRIMARY)


def main():
    with io.open(README, encoding="utf-8") as f:
        text = f.read()

    changed = []

    if "<!--UPGRADE-HEADER-->" not in text:
        lines = text.split("\n")
        idx = next((i for i, l in enumerate(lines) if l.startswith("# ")), None)
        if idx is None:
            lines.insert(0, HEADER)
        else:
            lines.insert(idx + 1, HEADER)
        text = "\n".join(lines)
        changed.append("badge header")

    if "<!--UPGRADE-REPOS-->" not in text:
        marker = "## System architecture"
        if marker in text:
            text = text.replace(marker, REPOS.strip() + "\n\n" + marker, 1)
        else:
            text = text.rstrip() + "\n\n" + REPOS
        changed.append("repository section")

    if "<!--UPGRADE-CITE-->" not in text:
        text = text.rstrip() + "\n\n" + CITE
        changed.append("citation + licence")

    if not changed:
        print("Nothing to do - README is already upgraded.")
        return

    with io.open(README, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)

    print("Added: " + ", ".join(changed))
    print("README is now %d lines" % (text.count("\n") + 1))


if __name__ == "__main__":
    main()
