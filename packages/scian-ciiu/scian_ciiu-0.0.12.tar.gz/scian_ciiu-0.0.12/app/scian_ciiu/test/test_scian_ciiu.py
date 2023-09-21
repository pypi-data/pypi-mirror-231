from unittest import TestCase
from ..src.scian_ciiu import (
    scian_id_to_ciiu,
    scian_string_to_ciiu,
    ciiu_id_to_scian,
    ciiu_string_to_scian,
)


class GeneratorTest(TestCase):
    def test_scian_id_to_ciiu(self) -> None:
        test_scian = "111219"
        expected_result = {
            "0113": [
                "Cultivo de hortalizas y melones, raíces y tubérculos (cultivo de "
                "brócoli, zanahorias, lechuga, espárrago, nopal, pepino, y otras "
                "hortalizas n.c.p.*)"
            ],
            "0119": [
                "Cultivo de otros productos agrícolas no perennes (cultivo de otras "
                "hortalizas no perenes n.c.p.*)"
            ],
        }

        r = scian_id_to_ciiu(test_scian)
        self.assertDictEqual(r, expected_result)

    def test_scian_string_to_ciiu(self) -> None:
        test_scian = "Cultivo"
        expected_result = {
            "0111": [
                "Cultivo de cereales (excepto arroz), leguminosas y semillas oleaginosas (cultivo de soya)",
                "Cultivo de cereales (excepto arroz), leguminosas y semillas oleaginosas (cultivo de cártamo)",
                "Cultivo de cereales (excepto arroz), leguminosas y semillas oleaginosas (cultivo de girasol)",
                "Cultivo de cereales (excepto arroz), leguminosas y semillas oleaginosas (cultivo de canola, higuerilla, linaza, ajonjolí, colza y otras semillas oleaginosas anuales n.c.p.*)",
                "Cultivo de cereales (excepto arroz), leguminosas y semillas oleaginosas (cultivo de frijol grano)",
                "Cultivo de cereales (excepto arroz), leguminosas y semillas oleaginosas (cultivo de garbanzo grano)",
                "Cultivo de cereales (excepto arroz), leguminosas y semillas oleaginosas (cultivo de lenteja, arvejón, haba y otras leguminosas para grano n.c.p.*)",
                "Cultivo de cereales (excepto arroz), leguminosas y semillas oleaginosas (cultivo de trigo)",
                "Cultivo de cereales (excepto arroz), leguminosas y semillas oleaginosas (cultivo de maíz grano)",
                "Cultivo de cereales (excepto arroz), leguminosas y semillas oleaginosas (cultivo de sorgo grano)",
                "Cultivo de cereales (excepto arroz), leguminosas y semillas oleaginosas (cultivo de avena grano)",
                "Cultivo de cereales (excepto arroz), leguminosas y semillas oleaginosas (cultivo de cebada grano)",
                "Cultivo de cereales (excepto arroz), leguminosas y semillas oleaginosas (cultivo de sorgo forrajero)",
                "Cultivo de cereales (excepto arroz), leguminosas y semillas oleaginosas (cultivo de avena forrajera)",
                "Cultivo de cereales (excepto arroz), leguminosas y semillas oleaginosas (cultivo de centeno, mijo, arroz silvestre y otros cereales n.c.p.*)",
                "Cultivo de cereales (excepto arroz), leguminosas y semillas oleaginosas (cultivo de cacahuate)",
                "Cultivo de cereales (excepto arroz), leguminosas y semillas oleaginosas (cultivo de diferentes especies vegetales cuando sea imposible determinar la actividad principal)",
            ],
            "0119": [
                "Cultivo de otros productos agrícolas no perennes (cultivo de maíz forrajero)",
                "Cultivo de otros productos agrícolas no perennes (cultivo de otras hortalizas no perenes n.c.p.*)",
                "Cultivo de otros productos agrícolas no perennes (cultivo de alfalfa)",
                "Cultivo de otros productos agrícolas no perennes (cultivo de pastos)",
                "Cultivo de otros productos agrícolas no perennes (cultivo de semillas de plantas forrajeras y de semillas de flores)",
            ],
            "0112": ["Cultivo de arroz "],
            "0113": [
                "Cultivo de hortalizas y melones, raíces y tubérculos (cultivo de jitomate o tomate rojo)",
                "Cultivo de hortalizas y melones, raíces y tubérculos (cultivo de cebolla)",
                "Cultivo de hortalizas y melones, raíces y tubérculos (cultivo de melón)",
                "Cultivo de hortalizas y melones, raíces y tubérculos (cultivo de tomate verde)",
                "Cultivo de hortalizas y melones, raíces y tubérculos (cultivo de papa)",
                "Cultivo de hortalizas y melones, raíces y tubérculos (cultivo de calabaza)",
                "Cultivo de hortalizas y melones, raíces y tubérculos (cultivo de sandía)",
                "Cultivo de hortalizas y melones, raíces y tubérculos (cultivo de brócoli, zanahorias, lechuga, espárrago, nopal, pepino, y otras hortalizas n.c.p.*)",
                "Cultivo de hortalizas y melones, raíces y tubérculos (cultivo de jitomate en invernaderos y otras estructuras agrícolas protegidas)",
                "Cultivo de hortalizas y melones, raíces y tubérculos (cultivo de pepino en invernaderos y otras estructuras agrícolas protegidas)",
                "Cultivo de hortalizas y melones, raíces y tubérculos (cultivo de acelga, berenjena, calabacitas, chícharos, hongos, lechuga, nopal verdura, rabanito, verdolaga, zanahoria y otros cultivos en invernaderos y otras estructuras agrícolas protegidas n.c.p.*)",
                "Cultivo de hortalizas y melones, raíces y tubérculos (cultivo de remolacha azucarera)",
            ],
            "0128": [
                "Cultivo de especias y de plantas aromáticas, medicinales y farmacéuticas (cultivo de chile)",
                "Cultivo de especias y de plantas aromáticas, medicinales y farmacéuticas (cultivo de chile en invernaderos y otras estructuras agrícolas protegidas)",
                "Cultivo de especias y de plantas aromáticas, medicinales y farmacéuticas (cultivo de albahaca en invernaderos y otras estructuras agrícolas protegidas)",
                "Cultivo de especias y de plantas aromáticas, medicinales y farmacéuticas (cultivo de especias)",
            ],
            "0123": [
                "Cultivo de cítricos (cultivo de naranja)",
                "Cultivo de cítricos (cultivo de limón)",
                "Cultivo de cítricos (cultivo de toronja, mandarina, lima, tangerina, cidra, y otros cítricos n.c.p.*)",
            ],
            "0127": [
                "Cultivo de plantas con las que se preparan bebidas (cultivo de café)",
                "Cultivo de plantas con las que se preparan bebidas (cultivo de cacao)",
                "Cultivo de plantas con las que se preparan bebidas (cultivo de agaves alcoholeros)",
                "Cultivo de plantas con las que se preparan bebidas (cultivo de té)",
            ],
            "0122": [
                "Cultivo de frutas tropicales y subtropicales (cultivo de plátano)",
                "Cultivo de frutas tropicales y subtropicales (cultivo de mango)",
                "Cultivo de frutas tropicales y subtropicales (cultivo de aguacate)",
                "Cultivo de frutas tropicales y subtropicales (cultivo de papaya y piña)",
                "Cultivo de frutas tropicales y subtropicales (cultivo de otras frutas tropicales y subtropicales en invernaderos y otras estructuras agrícolas protegidas n.c.p.*)",
            ],
            "0121": ["Cultivo de uva "],
            "0124": [
                "Cultivo de frutas de pepita y de hueso (cultivo de manzana)",
                "Cultivo de frutas de pepita y de hueso (cultivo de ciruelas, guayaba, duraznos, zapotes y peras)",
                "Cultivo de frutas de pepita y de hueso (cultivo de manzana en invernaderos y otras estructuras agrícolas protegidas)",
            ],
            "0126": [
                "Cultivo de frutos oleaginosos (cultivo de coco)",
                "Cultivo de frutos oleaginosos (cultivo de olivo)",
            ],
            "0125": [
                "Cultivo de otros frutos y nueces de árboles y arbustos (cultivo de mora, fresa, kiwi, nueces, piñón, avellana, y otros frutales no cítricos n.c.p.*)",
                "Cultivo de otros frutos y nueces de árboles y arbustos (cultivo de fresa en invernaderos y otras estructuras agrícolas protegidas)",
                "Cultivo de otros frutos y nueces de árboles y arbustos [cultivo de bayas (berries) en invernaderos y otras estructuras agrícolas protegidas, excepto fresas]",
                "Cultivo de otros frutos y nueces de árboles y arbustos (cultivo de semilla mejorada de fruta)",
            ],
            "0130": [
                "Propagación de plantas (producción de plántulas y plantitas de hortalizas en almácigos en invernaderos y otras estructuras agrícolas protegidas)",
                "Propagación de plantas (cultivo de sarmientos, bulbos, patrones, estacas, hijuelos y plantas jóvenes en invernaderos y otras estructuras agrícolas protegidas)",
                "Propagación de plantas (cultivo de pasto en rollo)",
            ],
            "0129": [
                "Cultivo de otras plantas perennes (cultivo de árboles de ciclo productivo de 10 años o menos)",
                "Cultivo de otras plantas perennes (cultivo de árboles para la recolección de caucho, de sabia, gomas y resinas)",
            ],
            "0115": ["Cultivo de tabaco "],
            "0116": [
                "Cultivo de plantas para fibras textiles (cultivo de algodón)",
                "Cultivo de plantas para fibras textiles (cultivo de yute, lino, sisal, ramio y fibras naturales similares)",
            ],
            "0114": ["Cultivo de caña de azúcar "],
            "0164": ["Tratamiento de semillas para propagación "],
            "0230": [
                "Recolección de productos forestales distintos de la madera (recolección de sabia de maple)"
            ],
        }

        r = scian_string_to_ciiu(test_scian)
        self.assertDictEqual(r, expected_result)

    def test_ciiu_id_to_scian(self) -> None:
        test_scian = "0111"
        expected_result = {
            "111110": ["Cultivo de soya"],
            "111121": ["Cultivo de cártamo"],
            "111122": ["Cultivo de girasol"],
            "111129": ["Cultivo anual de otras semillas oleaginosas"],
            "111131": ["Cultivo de frijol grano"],
            "111132": ["Cultivo de garbanzo grano"],
            "111139": ["Cultivo de otras leguminosas"],
            "111140": ["Cultivo de trigo"],
            "111151": ["Cultivo de maíz grano"],
            "111191": ["Cultivo de sorgo grano"],
            "111192": ["Cultivo de avena grano"],
            "111193": ["Cultivo de cebada grano"],
            "111194": ["Cultivo de sorgo forrajero"],
            "111195": ["Cultivo de avena forrajera"],
            "111199": ["Cultivo de otros cereales"],
            "111992": ["Cultivo de cacahuate"],
            "111999": ["Otros cultivos"],
        }

        r = ciiu_id_to_scian(test_scian)
        self.assertDictEqual(r, expected_result)

    def test_ciiu_string_to_scian(self) -> None:
        test_scian = "Cultivo"
        expected_result = {
            "111110": ["Cultivo de soya"],
            "111121": ["Cultivo de cártamo"],
            "111122": ["Cultivo de girasol"],
            "111129": ["Cultivo anual de otras semillas oleaginosas"],
            "111131": ["Cultivo de frijol grano"],
            "111132": ["Cultivo de garbanzo grano"],
            "111139": ["Cultivo de otras leguminosas"],
            "111140": ["Cultivo de trigo"],
            "111151": ["Cultivo de maíz grano"],
            "111152": ["Cultivo de maíz forrajero"],
            "111160": ["Cultivo de arroz"],
            "111191": ["Cultivo de sorgo grano"],
            "111192": ["Cultivo de avena grano"],
            "111193": ["Cultivo de cebada grano"],
            "111194": ["Cultivo de sorgo forrajero"],
            "111195": ["Cultivo de avena forrajera"],
            "111199": ["Cultivo de otros cereales"],
            "111211": ["Cultivo de jitomate o tomate rojo"],
            "111212": ["Cultivo de chile"],
            "111213": ["Cultivo de cebolla"],
            "111214": ["Cultivo de melón"],
            "111215": ["Cultivo de tomate verde"],
            "111216": ["Cultivo de papa"],
            "111217": ["Cultivo de calabaza"],
            "111218": ["Cultivo de sandía"],
            "111219": ["Cultivo de otras hortalizas"],
            "111310": ["Cultivo de naranja"],
            "111321": ["Cultivo de limón"],
            "111329": ["Cultivo de otros cítricos"],
            "111331": ["Cultivo de café"],
            "111332": ["Cultivo de plátano"],
            "111333": ["Cultivo de mango"],
            "111334": ["Cultivo de aguacate"],
            "111335": ["Cultivo de uva"],
            "111336": ["Cultivo de manzana"],
            "111337": ["Cultivo de cacao"],
            "111338": ["Cultivo de coco"],
            "111339": ["Cultivo de otros frutales no cítricos y de nueces"],
            "111411": [
                "Cultivo de jitomate en invernaderos y otras estructuras agrícolas protegidas"
            ],
            "111412": [
                "Cultivo de fresa en invernaderos y otras estructuras agrícolas protegidas"
            ],
            "111413": [
                "Cultivo de bayas (berries) en invernaderos y otras estructuras agrícolas protegidas, excepto fresas"
            ],
            "111414": [
                "Cultivo de chile en invernaderos y otras estructuras agrícolas protegidas"
            ],
            "111415": [
                "Cultivo de manzana en invernaderos y otras estructuras agrícolas protegidas"
            ],
            "111416": [
                "Cultivo de pepino en invernaderos y otras estructuras agrícolas protegidas"
            ],
            "111419": [
                "Cultivo de otros productos alimenticios en invernaderos y otras estructuras agrícolas protegidas"
            ],
            "111421": ["Floricultura a cielo abierto"],
            "111422": [
                "Floricultura en invernaderos y otras estructuras agrícolas protegidas"
            ],
            "111423": ["Cultivo de árboles de ciclo productivo de 10 años o menos"],
            "111429": [
                "Otros cultivos no alimenticios en invernaderos y otras estructuras agrícolas protegidas"
            ],
            "111910": ["Cultivo de tabaco"],
            "111920": ["Cultivo de algodón"],
            "111930": ["Cultivo de caña de azúcar"],
            "111941": ["Cultivo de alfalfa"],
            "111942": ["Cultivo de pastos"],
            "111991": ["Cultivo de agaves alcoholeros"],
            "111992": ["Cultivo de cacahuate"],
            "111993": ["Actividades agrícolas combinadas con explotación de animales"],
            "111994": ["Actividades agrícolas combinadas con aprovechamiento forestal"],
            "111995": [
                "Actividades agrícolas combinadas con explotación de animales y aprovechamiento forestal"
            ],
            "111999": ["Otros cultivos"],
            "112991": [
                "Explotación de animales combinada con aprovechamiento forestal"
            ],
        }

        r = ciiu_string_to_scian(test_scian)
        self.assertDictEqual(r, expected_result)
