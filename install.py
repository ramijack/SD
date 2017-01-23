import Conditions
from bin import Download
from bin import AppInstall


def run_package():
    # Download conditions
    download_conditions_met = Conditions.minimum_ram_required(8, "GB") and \
                              Conditions.minimum_disk_space(10, "GB") and \
                              Conditions.is_power_on_battery()

    if not download_conditions_met:
        return "Download Conditions Failed"

    Download.download_all_apps()

    install_conditions_met = Conditions.minimum_ram_required(8, "GB") and \
                             Conditions.minimum_disk_space(10, "GB") and \
                             Conditions.is_power_on_battery()

    if not install_conditions_met:
        return "Install Conditions Failed"

    AppInstall.app_install('test')


print run_package()
