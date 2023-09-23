import click

# ovos-gui
from ovos_gui.service import GUIService

# ovos-dinkum-listener
from ovos_dinkum_listener.service import OVOSDinkumVoiceService
from ovos_listener.service import SpeechService
from mycroft_classic_listener.service import ClassicListener

# ovos-core
from ovos_utils.skills.api import SkillApi
from ovos_workshop.skills.fallback import FallbackSkill
from ovos_bus_client.util.scheduler import EventScheduler
from ovos_core.intent_services import IntentService
from ovos_core.skill_manager import SkillManager

# ovos-messagebus
from ovos_messagebus.load_config import load_message_bus_config
from ovos_messagebus import MessageBusEventHandler
from tornado import web

# ovos-audio
from ovos_audio.service import PlaybackService

# misc ovos
from ovos_bus_client import MessageBusClient
from ovos_config.locale import setup_locale
from ovos_utils import wait_for_exit_signal
from ovos_utils.log import LOG, init_service_logger
from ovos_utils.process_utils import reset_sigint_handler, PIDLock


def on_ready():
    LOG.info('OVOS Launcher started!')


def on_error(e='Unknown'):
    LOG.info('OVOS Launcher failed to start ({})'.format(repr(e)))


def on_stopping():
    LOG.info('OVOS Launcher is shutting down...')


@click.command()
@click.option("--listener", "-l", default="dinkum",
              help="Choose a listener for mic input handling, dinkum/old/classic")
def launch(listener):
    main(listener=listener)


def main(listener="dinkum", ready_hook=on_ready, error_hook=on_error, stopping_hook=on_stopping):
    LOG.info('Starting OVOS Launcher')

    init_service_logger("ovos-launcher")
    reset_sigint_handler()
    PIDLock("ovos-launcher")
    setup_locale()

    # bus service
    LOG.info('Starting message bus service...')
    config = load_message_bus_config()
    routes = [(config.route, MessageBusEventHandler)]
    application = web.Application(routes)
    application.listen(config.port, config.host)

    # line below not needed because we run GUIService further down
    # create_daemon(ioloop.IOLoop.instance().start)

    # bus client
    bus = MessageBusClient()
    bus.run_in_thread()

    # GUI service
    LOG.info('Starting GUI bus service...')
    gui = GUIService()
    gui.run()

    # Audio output service
    LOG.info('Starting audio service...')
    audio = PlaybackService()
    audio.daemon = True
    audio.start()

    # STT service
    LOG.info('Starting STT service...')
    if listener == "classic":
        service = ClassicListener(bus)
    elif listener == "old":
        service = SpeechService()
    else:
        service = OVOSDinkumVoiceService()
    service.daemon = True
    service.start()

    # Skills service
    LOG.info('Starting Skills service...')
    intents = IntentService(bus)
    # Register handler to trigger fallback system
    bus.on(
        'mycroft.skills.fallback',
        FallbackSkill.make_intent_failure_handler(bus)
    )

    event_scheduler = EventScheduler(bus, autostart=False)
    event_scheduler.daemon = True
    event_scheduler.start()

    SkillApi.connect_bus(bus)

    skill_manager = SkillManager(bus)
    skill_manager.start()

    # wait until ctrl+c to exit
    ready_hook()
    wait_for_exit_signal()

    # shutdown cleanly
    audio.shutdown()
    gui.stop()
    if event_scheduler is not None:
        event_scheduler.shutdown()
    if skill_manager is not None:
        skill_manager.stop()
        skill_manager.join()
    stopping_hook()


if __name__ == "__main__":
    launch
