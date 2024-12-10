using System.IO;

namespace SharedCode
{
    public static class SharedFunctions
    {
        public static int GetCurrentPhase()
        {

            var filePath = System.IO.Path.Combine(Directory.GetCurrentDirectory(), "wwwroot", "Database", "currentPhase.txt");

            using (StreamReader sr = new StreamReader(filePath))
            {

                string? line = sr.ReadLine();
                if (int.TryParse(line, out int result))
                {
                    return result;
                }
                else
                {
                    throw new InvalidOperationException("The file is empty, the line is null, or it does not contain a valid integer.");
                }

            }
        }
    }
}