using System.IO;

namespace SharedCode
{
    public static class SharedFunctions
    {
        public static int GetCurrentPhase(){

            var filePath = System.IO.Path.Combine(Directory.GetCurrentDirectory(), "wwwroot", "Database", "currentPhase.txt");

            using (StreamReader sr = new StreamReader(filePath))
            {

                return int.Parse(sr.ReadLine());

            }
        }
    }
}