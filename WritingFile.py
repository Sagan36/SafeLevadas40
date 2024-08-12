# 2023-2024 Programacao 2 LTI
# Grupo 40
# 62269 Dinis Garcia
# 62238 Afonso Paulo

from File import File

class WritingFile(File):
    '''
    Writes the file.
    '''
    def WritingOutPutFile(self,output_file, content):
        """
        Writes the output data to the file in a specific way.

        Requires:
        output_file is a string that has the name of the OutputFile
        content is a dictionary with the paths data to write to the file
        Ensures:
        The output file is written with the specified formatting
        """
        with open(output_file, 'w') as file:
            for key, value in content.items():
                file.write(key + '\n')
                for path in value:
                    if isinstance(path, list):
                        weight = path[0]
                        stations = ', '.join(path[1])
                        file.write(f"{weight}, {stations}"'\n')
                    else:
                        file.write(f"{path}"'\n')
            




